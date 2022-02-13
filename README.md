# auto_add_role.discord.py
自己紹介を記入したときに、自動的に“メンバー“ロールを付与します。

1. ```bash
sudo apt install python3-pip```  
2. ```bash
pip3 install python-dotenv discord.py
```
3. ```bash
vim .env  
```
```bash
DISCORD_TOKEN="your-token"
DISCORD_VOL_ROLE="付与したいロールのID
```

4. ```bash
./bot.py
```
