import ctypes
import shutil
import sys
import time

# ==================== SETTINGS ====================
TARGET_X = 100  # Target X coordinate
TARGET_Y = 240  # Target Y coordinate
TOLERANCE = 30  # Tolerance in pixels (+- TOLERANCE)
CHECK_INTERVAL_MS = 500  # Check interval in milliseconds (1000 = 1 sec)

ENABLE_WINDOW_TITLE = True  # Flag: duplicate timer in the console window title
# ==================================================


class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]


def enable_dpi_awareness() -> None:
    """Enable DPI awareness for accurate coordinate reading on multi-monitor setups."""
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass


def set_console_title(title: str) -> None:
    """Set the Windows console window title."""
    try:
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    except Exception:
        pass


def get_mouse_position() -> tuple[int, int]:
    """Return global X and Y coordinates of the mouse cursor."""
    pt = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y


def is_in_target_zone(
    x: int, y: int, target_x: int, target_y: int, tolerance: int
) -> bool:
    """Check if a point falls within a square region (target ± tolerance)."""
    return abs(x - target_x) <= tolerance and abs(y - target_y) <= tolerance


def format_time(seconds_total: float) -> str:
    """Format elapsed seconds into HH:MM:SS format."""
    total_sec = int(seconds_total)
    hours, remainder = divmod(total_sec, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def main() -> None:
    enable_dpi_awareness()

    interval_sec = CHECK_INTERVAL_MS / 1000.0

    print("=== Auto-Reset Console Timer ===")
    print(f"Target area: X={TARGET_X}, Y={TARGET_Y} (±{TOLERANCE}px)")
    print(f"Polling interval: {CHECK_INTERVAL_MS} ms")
    print("Press Ctrl+C to exit.\n")

    reset_timestamp = time.monotonic()

    try:
        while True:
            x, y = get_mouse_position()

            in_zone = is_in_target_zone(x, y, TARGET_X, TARGET_Y, TOLERANCE)
            if in_zone:
                reset_timestamp = time.monotonic()

            elapsed_seconds = time.monotonic() - reset_timestamp
            time_str = format_time(elapsed_seconds)

            # 1. Update window title (if enabled)
            if ENABLE_WINDOW_TITLE:
                status_title = " [RESET]" if in_zone else ""
                set_console_title(
                    # f"Timer: {time_str}{status_title} | X={x}, Y={y}"
                    f"{time_str}{status_title}"
                )

            # 2. Safe console output accounting for current terminal width
            status_flag = "[RESET]" if in_zone else "       "
            full_line = f"Time: {time_str}  |  Mouse: X={x:6d}, Y={y:6d}  |  {status_flag}"

            # Get current console window width
            cols, _ = shutil.get_terminal_size(fallback=(80, 24))
            max_len = max(
                1, cols - 1
            )  # 1-char buffer prevents terminal auto-wrapping

            # Truncate string to window width and right-pad with spaces
            # to overwrite lingering characters when resizing the console
            printed_line = full_line[:max_len].ljust(max_len)

            sys.stdout.write(f"\r{printed_line}")
            sys.stdout.flush()

            time.sleep(interval_sec)

    except KeyboardInterrupt:
        if ENABLE_WINDOW_TITLE:
            set_console_title("Timer Stopped")
        print("\n\nExited successfully.")


if __name__ == "__main__":
    main()
