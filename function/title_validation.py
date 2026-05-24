import re

def is_valid_title_en(title, anime_en, original_name=None):
    if re.search(r'Dubs|dubs|Flute|flute|Lofi|lofi|Nightcore|nightcore|TABS|Version|version|Lyrics|lyrics|Storyboard|storyboard|Piano|piano|React|react|cover|instrumental|カバー|インストルメンタル', title, re.IGNORECASE):
        return False
                
    lenient_anime = re.sub(r'[^a-zA-Z0-9\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f]+', '.*', anime_en)
    pattern = rf'{lenient_anime}.*(Op|Opening|スペシャル)\s*\d*'
    if re.search(pattern, title, re.IGNORECASE):
        return True
    
    if original_name:
        lenient_orig = re.sub(r'[^a-zA-Z0-9\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f]+', '.*', original_name)
        pattern_orig = rf'{lenient_orig}.*(Op|Opening|スペシャル)\s*\d*'
        if re.search(pattern_orig, title, re.IGNORECASE):
            return True

    return False

def is_valid_title_jap(title, anime_jap, original_name=None):
    if re.search(r'Dubs|dubs|Flute|flute|Lofi|lofi|Nightcore|nightcore|TABS|Version|version|Lyrics|lyrics|Storyboard|storyboard|Piano|piano|React|react|cover|instrumental|カバー|インストルメンタル', title, re.IGNORECASE):
        return False
                
    lenient_anime = re.sub(r'[^a-zA-Z0-9\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f]+', '.*', anime_jap)
    pattern = rf'{lenient_anime}.*(Op|Opening|スペシャル)\s*\d*'
    if re.search(pattern, title, re.IGNORECASE):
        return True

    if original_name:
        lenient_orig = re.sub(r'[^a-zA-Z0-9\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f]+', '.*', original_name)
        pattern_orig = rf'{lenient_orig}.*(Op|Opening|スペシャル)\s*\d*'
        if re.search(pattern_orig, title, re.IGNORECASE):
            return True
            
    return False