import streamlit as st
import pandas as pd
import plotly.express as px

def create_visualization(df: pd.DataFrame) -> None:
    """Create all dashboard visualizations"""
    if len(df) > 0:
        # Protocol distribution
        protocol_counts = df['protocol'].value_counts()
        fig_protocol = px.pie(
            values=protocol_counts.values,
            names=protocol_counts.index,
            title='Protocol Distribution'
        )
        st.plotly_chart(fig_protocol, use_container_width=True)
        
        # Packet timeline
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df_grouped = df.groupby(df['timestamp'].dt.floor('s')).size()
        fig_timeline = px.line(
            x=df_grouped.index,
            y=df_grouped.values,
            title='Packets per second'
        )
        st.plotly_chart(fig_timeline, use_container_width=True)