import React from 'react'
import './TradingLogs.css'

interface LogProps {
    logs: [string];
}

function TradingLogs({ logs }: LogProps) {
    return (
        <div className='logsContainer'>
            <div className='logItem title'>진행된 자동 거래 기록을 조회합니다.</div>
            { logs.map((log) => <div className='logItem' key={log}>{log}</div>) }
        </div>
    )
}

export default TradingLogs