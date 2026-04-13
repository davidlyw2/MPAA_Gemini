import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sqlite3
import os

# DB 경로 설정
RESULT_DB = "MPAA_Result.db"

app = dash.Dash(__name__, update_title=None)

# 대시보드 레이아웃
app.layout = html.Div([
    html.Div([
        html.H1("📊 MPAA V3.1 퀀트 분석 대시보드", style={'textAlign': 'center', 'paddingTop': '20px'}),
        
        # 상단 컨트롤: 기간 선택
        html.Div([
            html.Label("📅 분석 기간 설정: ", style={'fontWeight': 'bold'}),
            dcc.DatePickerRange(
                id='date-picker',
                display_format='YYYY-MM-DD',
                style={'marginLeft': '10px'}
            ),
            dcc.RadioItems(
                id='period-selector',
                options=[
                    {'label': '전체', 'value': 'ALL'},
                    {'label': '1년', 'value': '1Y'},
                    {'label': '3년', 'value': '3Y'}
                ],
                value='ALL',
                inline=True,
                style={'display': 'inline-block', 'marginLeft': '30px'}
            )
        ], style={'backgroundColor': '#f9f9f9', 'padding': '15px', 'borderRadius': '10px', 'margin': '10px 0'}),

        # 메인 그래프 영역 (화면 꽉 차게 설정)
        dcc.Graph(
            id='main-charts', 
            style={'height': '75vh', 'width': '100%'}, # 세로를 화면 높이의 75%로 설정
            config={'responsive': True}
        ),

        # 하단 상세 정보 영역
        html.Div(id='detail-info-display', style={'padding': '20px', 'marginTop': '10px', 'borderTop': '2px solid #eee'})
    ], style={'width': '98%', 'margin': '0 auto'}) # 창 너비 최대 활용
])

@app.callback(
    Output('main-charts', 'figure'),
    [Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date'),
     Input('period-selector', 'value')]
)
def update_graphs(start_date, end_date, period):
    if not os.path.exists(RESULT_DB):
        return go.Figure()

    conn = sqlite3.connect(RESULT_DB)
    df = pd.read_sql("SELECT * FROM daily_metrics ORDER BY date", conn)
    conn.close()
    
    df['date'] = pd.to_datetime(df['date'])

    # 기간 필터링
    if period == '1Y':
        df = df[df['date'] > (df['date'].max() - pd.DateOffset(years=1))]
    elif period == '3Y':
        df = df[df['date'] > (df['date'].max() - pd.DateOffset(years=3))]
    
    if start_date and end_date:
        df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

    fig = make_subplots(
        rows=2, cols=1, 
        shared_xaxes=True, 
        vertical_spacing=0.08, # 간격 최적화
        subplot_titles=("📈 누적 수익률", "⚠️ 리스크 지표 (MDD & Sharpe)"),
        specs=[[{"secondary_y": False}], [{"secondary_y": True}]]
    )

    # 상단
    fig.add_trace(go.Scatter(x=df['date'], y=df['cum_return'], name="누적수익률", line=dict(color='#1f77b4', width=2)), row=1, col=1)
    
    # 하단
    fig.add_trace(go.Scatter(x=df['date'], y=df['drawdown']*100, name="MDD (%)", fill='tozeroy', line=dict(color='#ef553b')), row=2, col=1)
    fig.add_trace(go.Scatter(x=df['date'], y=df['sharpe'], name="Sharpe", line=dict(color='#00cc96', dash='dot')), row=2, col=1, secondary_y=True)

    fig.update_layout(
        margin=dict(l=40, r=40, t=60, b=40),
        hovermode='x unified',
        template='plotly_white',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig

@app.callback(
    Output('detail-info-display', 'children'),
    [Input('main-charts', 'clickData')]
)
def display_click_data(clickData):
    if not clickData:
        return html.H4("☝️ 차트의 특정 날짜를 클릭하면 상세 비중이 표시됩니다.", style={'textAlign': 'center', 'color': '#999'})
    
    # 클릭한 날짜 추출 (형식: 2023-10-23)
    raw_date = clickData['points'][0]['x'].split(' ')[0]
    
    conn = sqlite3.connect(RESULT_DB)
    # LIKE 연산자를 사용하여 시분초가 붙어있어도 날짜만으로 검색
    query = "SELECT code, weight FROM daily_weights WHERE date LIKE ?"
    df_w = pd.read_sql(query, conn, params=(f"{raw_date}%",))
    conn.close()
    
    if df_w.empty:
        return html.Div([
            html.P(f"❌ {raw_date}: 비중 데이터가 없습니다. (DB 재생성 필요)", style={'color': 'red', 'textAlign': 'center'})
        ])

    # 비중 기준 내림차순 정렬
    df_w = df_w.sort_values(by='weight', ascending=False)

    # 테이블 렌더링
    table_header = [html.Thead(html.Tr([html.Th("자산 코드"), html.Th("비중 (%)")], style={'backgroundColor': '#f2f2f2'}))]
    table_body = [html.Tbody([
        html.Tr([
            html.Td(row['code'], style={'padding': '10px', 'borderBottom': '1px solid #ddd'}),
            html.Td(f"{row['weight']*100:.2f}%", style={'padding': '10px', 'borderBottom': '1px solid #ddd', 'fontWeight': 'bold'})
        ]) for _, row in df_w.iterrows()
    ])]

    return html.Div([
        html.H3(f"📅 {raw_date} 투자 포트폴리오", style={'marginBottom': '15px'}),
        html.Table(table_header + table_body, style={'width': '100%', 'borderCollapse': 'collapse', 'fontSize': '16px'})
    ])

if __name__ == '__main__':
    app.run(debug=True)