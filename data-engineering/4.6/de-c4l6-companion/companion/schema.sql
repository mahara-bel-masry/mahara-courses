-- مخطط قاعدة بيانات السكرابر: نفس مفاهيم كورس 3
PRAGMA foreign_keys = ON;  -- للـ sqlite3 CLI؛ في بايثون السكربت بيفعلها لكل اتصال بنفسه

CREATE TABLE IF NOT EXISTS runs (
    run_id       INTEGER PRIMARY KEY,
    run_at_utc   TEXT NOT NULL,          -- توقيت عالمي زي ما اتفقنا في درس 5
    status       TEXT NOT NULL,          -- ok / failed
    quotes_found INTEGER NOT NULL DEFAULT 0,
    quotes_new   INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS quotes (
    quote_id INTEGER PRIMARY KEY,
    run_id   INTEGER NOT NULL REFERENCES runs(run_id),
    text     TEXT NOT NULL,
    author   TEXT NOT NULL,
    UNIQUE(text, author)                 -- منع التكرار على مستوى القاعدة
);
