import re

def choice(selected_video_link_jap, selected_video_link_en, title_jap, title_en):

    if selected_video_link_jap:
        title_jap_n = re.search(r'\d+', title_jap)

    if selected_video_link_jap is not None and title_jap_n is not None:
        final_title = title_jap
        final_link = selected_video_link_jap
    
    else:
        final_title = title_en
        final_link = selected_video_link_en
             
    return final_link, final_title