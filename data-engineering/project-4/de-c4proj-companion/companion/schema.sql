-- مشروع كورس 4: سكرابر أسعار يومي + ملخص يومي
-- بيتطبع تلقائي أول تشغيلة، محطوط هنا للقراءة والمراجعة
PRAGMA foreign_keys = ON;  -- للـ sqlite3 CLI؛ في بايثون السكربت بيفعلها لكل اتصال بنفسه

CREATE TABLE IF NOT EXISTS runs (
  run_id     INTEGER PRIMARY KEY,
  run_at_utc TEXT NOT NULL,
  status     TEXT NOT NULL,
  pages_ok   INTEGER NOT NULL DEFAULT 0,
  books_found INTEGER NOT NULL DEFAULT 0,
  books_new  INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS books (
  book_key        TEXT PRIMARY KEY,
  title      TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS snapshots (
  run_id     INTEGER NOT NULL REFERENCES runs(run_id),
  book_key        TEXT NOT NULL REFERENCES books(book_key),
  price_gbp  REAL NOT NULL,
  rating     INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
  PRIMARY KEY (run_id, book_key)
);
