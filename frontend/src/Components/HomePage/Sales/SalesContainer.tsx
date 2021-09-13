import React from 'react'
import './SalesContainer.css'

function SalesContainer() {
    return (
        <div className='salesContainer'>
            <div className='salesTitle'>주문 설정</div>
            <div className='salesInfoContainer coinInfo'>
                {/* from server */}
                <span>Coin Name</span> 
                <span>Current Price</span>
            </div>
            <div className='salesInfoContainer aspectInfo'>
                <span>추정 수익률</span>
                {/* from server */}
                <span>추정률 값</span>
            </div>
            <div className='salesItemContainer'>
                <div className='salesItemTitle'>매도 손절율</div>
                <div className='salesItemDescription'>해당 %만큼 손해가 발생했을 때 자동으로 판매합니다.</div>
                <input type='number' placeholder='%' className='inputSales'/>
            </div>
            <div className='salesItemContainer'>
                <div className='salesItemTitle'>매도 금액</div>
                <div className='salesItemDescription'>해당 금액에 도달했을 때 자동으로 판매합니다.</div>
                <input type='number'placeholder='원' className='inputSales'/>
            </div>
            <div className='buttonContainer'>
                <button type='button' className='requestBtn'>손절 정보 설정</button>
            </div>
        </div>
    )
}

export default SalesContainer