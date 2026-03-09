import streamlit as st
import streamlit.components.v1 as components
import os

# Streamlit 페이지 설정
st.set_page_config(page_title="보드게임 서버", layout="wide")

def main():
    st.title("🎮 오목 보드게임")
    
    # htmls/index.html 파일 경로 설정
    # 현재 파일(app.py) 위치를 기준으로 경로를 찾습니다.
    base_path = os.path.dirname(__file__)
    html_file_path = os.path.join(base_path, 'htmls', 'index.html')

    try:
        # index.html 파일을 읽어옵니다.
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Streamlit 화면에 HTML 컴포넌트를 출력합니다.
        # height는 게임판 크기에 맞춰 700px 정도로 설정했습니다.
        components.html(html_content, height=700, scrolling=True)
        
        st.success("게임이 성공적으로 로드되었습니다!")
        
    except FileNotFoundError:
        st.error(f"오류: '{html_file_path}' 파일을 찾을 수 없습니다. 폴더 구조를 확인해 주세요.")
    except Exception as e:
        st.error(f"예기치 못한 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    main()
