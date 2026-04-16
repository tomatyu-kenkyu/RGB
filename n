import streamlit as st

st.title("RGBペア 共通抽出ツール")

st.write("形式： 234,239,241 : 242,244,241 （改行で複数入力）")

# 入力欄
group1_text = st.text_area("グループ1", height=200)
group2_text = st.text_area("グループ2", height=200)


def normalize_pair(pair):
    a, b = pair
    return tuple(sorted([tuple(a), tuple(b)]))


def parse_pairs(text):
    pairs = []
    lines = text.strip().split("\n")
    for line in lines:
        if ":" in line:
            left, right = line.split(":")
            a = list(map(int, left.strip().split(",")))
            b = list(map(int, right.strip().split(",")))
            pairs.append((a, b))
    return pairs


def get_common_pairs(group1, group2):
    set1 = set(normalize_pair(p) for p in group1)
    set2 = set(normalize_pair(p) for p in group2)
    return list(set1 & set2)


def format_pairs(pairs):
    return "\n".join([f"{list(a)} : {list(b)}" for a, b in pairs])


# 実行ボタン
if st.button("共通ペアを抽出"):
    group1 = parse_pairs(group1_text)
    group2 = parse_pairs(group2_text)

    common = get_common_pairs(group1, group2)

    st.subheader("結果")

    if common:
        st.text(format_pairs(common))
    else:
        st.write("共通ペアはありません")