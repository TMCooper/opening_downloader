import re

def is_valid_title_en(title, anime_en):
    
    if re.search(r'Piano|piano|React|react|cover|instrumental|カバー|インストルメンタル', title, re.IGNORECASE):
        return False
                
    pattern = rf'{re.escape(anime_en)}.*(Op|Opening|スペシャル)\s*\d*'
    return re.search(pattern, title, re.IGNORECASE)

def is_valid_title_jap(title, anime_jap):
    
    if re.search(r'Piano|piano|React|react|cover|instrumental|カバー|インストルメンタル', title, re.IGNORECASE):
        return False
                
    pattern = rf'{re.escape(anime_jap)}.*(Op|Opening|スペシャル)\s*\d*'
    return re.search(pattern, title, re.IGNORECASE)