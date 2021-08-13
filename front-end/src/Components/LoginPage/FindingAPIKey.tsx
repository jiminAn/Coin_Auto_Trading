import React from 'react'
import './FindingAPIKey.css'

function FindingAPIKey() {
    return (
        <div className='findingContainer'>
            <div>bithumb API key가 기억나지 않으시나요?</div>
            <div>
                <a href='https://apidocs.bithumb.com/'>확인하기</a>
            </div>
        </div>
    )
}

export default FindingAPIKey