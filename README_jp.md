# RAG Project – Company Policy Q&A

RAG（Retrieval-Augmented Generation）の基本的な仕組みや処理の流れを学習・理解するために作成した、シンプルなRAGアプリケーションです。
会社の規定・ポリシーに関するドキュメントをナレッジベースとして使用し、ドキュメントをベクトル化してFAISSベクトルデータベースに保存します。ユーザーから質問を受けると、質問に関連性の高いドキュメントのチャンクをベクトル類似度検索によって取得し、取得したコンテキストのみをもとにOpenAIのLLMが回答を生成します。

> Note: 本プロジェクトは、RAGの仕組みを学習・理解するための学習・デモンストレーション目的で作成したものです。シンプルなRAGの実装例であり、エンタープライズ向けの本番環境で利用することを想定したシステムではありません。

# Features

- knowledge-base ディレクトリ内の .txt ファイルを読み込む
- ドキュメントを小さなチャンクに分割する
- OpenAIを使用してベクトル埋め込みを生成する
- 生成した埋め込みをFAISSベクトルデータベースに保存する
- ベクトル類似度検索により、質問に関連性の高いドキュメントチャンクを取得する
- OpenAI GPT-4.1-miniを使用して回答を生成する
- コマンドライン上で質問・回答を行うインタラクティブなインターフェースを提供する
- チャンクサイズ、オーバーラップ、取得するドキュメント数を設定可能

# File Description (ファイル構成)

app/config.py : モデル、RAG、パスなどの各種設定を記載
app/ingest.py : ドキュメントを読み込み、チャンクに分割し、埋め込みを生成してFAISSベクトルストアを構築
app/retrieve.py : FAISSベクトルストアを読み込み、関連性の高いドキュメントチャンクを検索
app/generate.py : プロンプトを作成し、OpenAIのLLMを使用して回答を生成
app/main.py : 対話形式のコマンドラインRAGアプリケーションを実行
data/documents/company_policy.txt : サンプルのナレッジベース用ドキュメント
data/vector_store/ : 生成されたFAISSベクトルストアを格納
.env : OpenAI APIキーを設定
requirements.txt : Pythonの依存ライブラリを記載

# Models

EMBEDDING_MODEL = "text-embedding-3-small"
LLM_MODEL = "gpt-4.1-mini"

# Set Up

> Prerequisites (事前準備): 
    - Pythonがインストールされていること
    - OpenAI APIキー

> Steps (セットアップ手順):
    - 仮想環境を作成 : python -m venv .venv
    - 仮想環境を有効化 : .venv\Scripts\activate
    - 必要なライブラリをインストール : pip install -r requirements.txt
    - OpenAI APIキーを設定 : ロジェクトルートにある .env ファイルにOpenAI APIキーを設定 : OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
    
    - ベクトルストアを作成 : 初回実行時、またはナレッジベースの内容を変更した場合は、まず、以下のコマンドを実行してください。 : python app/ingest.py
    - RAGアプリケーションを実行 : python app/main.py 
    - AGアプリケーションを終了 : exit

> Example test questions :
    - How many days of annual leave do employees receive?
    - What are the standard working hours?
    - How much notice is required before resignation?
    - What are the requirements for remote work?
    - How often are employee performance reviews conducted?
    - What security practices are mandatory?
