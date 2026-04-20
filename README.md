# 402 welcome site

## Quick start

```bash
cd /root/.openclaw/workspace/402-welcome-site
python3 -m http.server 8101 --bind 0.0.0.0
```

## Keep content read-only

```bash
cd /root/.openclaw/workspace/402-welcome-site
chmod 444 index.html styles.css script.js members.json README.md
chmod 555 .
```

> If you need to edit later, restore write permissions first.
