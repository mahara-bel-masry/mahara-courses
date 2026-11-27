class DataValidationError(Exception):
    """قاعدة قبول اتكسرت على صف أو ملف."""
    pass


class ConfigError(Exception):
    """ملف الإعدادات ناقص أو مكسور."""
    pass
