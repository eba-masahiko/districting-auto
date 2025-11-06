# 🇯🇵 districting-auto

**自動区割り生成システム（GerryChain + e-Stat + GitHub Actions + folium）**

## 概要
- e-Stat APIから人口を取得
- GerryChainで連続性を保った選挙区割りを自動生成
- 一票の格差 1.2倍以内を目標
- GitHub Actionsで週1回自動実行・更新
- Foliumで格差マップを自動生成してGitHub Pages公開

## 実行方法
```bash
export ESTAT_API_KEY=あなたのAPIキー
python src/main.py
```

## 出力
- outputs/summary.html（地図付き）
- outputs/metrics.csv（格差率データ）
- outputs/summary.png（静止画像）

## 公開ページ
`https://あなたのGitHubユーザ名.github.io/districting-auto/summary.html`
