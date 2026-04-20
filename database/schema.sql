-- 402 虚拟生活社区系统数据库结构

-- 成员表
CREATE TABLE IF NOT EXISTS members (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    role TEXT DEFAULT '402 成员',
    avatar_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 角色状态表
CREATE TABLE IF NOT EXISTS characters (
    user_id TEXT PRIMARY KEY,
    personality TEXT,
    ability TEXT,
    current_state TEXT DEFAULT 'normal',
    current_action TEXT,
    skin_id TEXT DEFAULT 'green_fish',
    FOREIGN KEY (user_id) REFERENCES members(id)
);

-- 树洞表
CREATE TABLE IF NOT EXISTS treehole (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    image_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_anonymous BOOLEAN DEFAULT 1
);

-- 地点表
CREATE TABLE IF NOT EXISTS locations (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    latitude REAL,
    longitude REAL
);

-- 照片表
CREATE TABLE IF NOT EXISTS photos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_id TEXT,
    url TEXT NOT NULL,
    caption TEXT,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (location_id) REFERENCES locations(id)
);

-- 聊天消息表
CREATE TABLE IF NOT EXISTS chat_messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    content TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES members(id)
);

-- 插入初始成员数据
INSERT OR REPLACE INTO members (id, name, role) VALUES
    ('chu', '初', '402 成员'),
    ('bo', '博', '402 成员'),
    ('hao', '昊', '402 成员'),
    ('qian', '千', '402 成员'),
    ('dong', '东', '402 成员'),
    ('zhu', '竹', '402 成员');

-- 插入初始角色数据
INSERT OR REPLACE INTO characters (user_id, personality, ability, skin_id) VALUES
    ('chu', '友好', '辅助', 'green_fish'),
    ('bo', '勇敢', '主C', 'green_fish'),
    ('hao', '聪明', '辅助', 'green_fish'),
    ('qian', '活泼', '近战', 'green_fish'),
    ('dong', '沉稳', '坦克', 'green_fish'),
    ('zhu', '温柔', '治疗', 'green_fish');
