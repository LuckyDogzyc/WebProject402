#!/usr/bin/env python3
"""数据库初始化脚本"""
import sqlite3
import os

def init_database():
    """初始化数据库"""
    db_path = os.path.join(os.path.dirname(__file__), '..', '..', 'database', 'community.db')
    schema_path = os.path.join(os.path.dirname(__file__), '..', '..', 'database', 'schema.sql')
    
    # 创建数据库目录
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # 读取 SQL 文件
    with open(schema_path, 'r', encoding='utf-8') as f:
        schema_sql = f.read()
    
    # 连接数据库并执行
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 分割 SQL 语句并执行
    for statement in schema_sql.split(';'):
        statement = statement.strip()
        if statement:
            cursor.execute(statement)
    
    conn.commit()
    conn.close()
    
    print(f"✅ 数据库初始化成功: {db_path}")
    return True

if __name__ == '__main__':
    init_database()
