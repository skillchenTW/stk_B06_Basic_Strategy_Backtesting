### 主要交易策略

#### 黃金交叉
-   黃金交叉是一種圖表模式，其中相對短期的移動平均線穿過長期移動平均線。黃金交叉是由涉及證券的短期移動平均線（例如 15 天移動平均線）突破其長期移動平均線（例如 50 天移動平均線）或阻力的交叉形成的看漲突破模式等級。由於長期指標具有更大的權重，黃金交叉表明牛市即將到來，並因高交易量而得到加強。

CrossOver
This indicator gives a signal if the provided datas (2) cross up or down.
1.0 if the 1st data crosses the 2nd data upwards
-1.0 if the 1st data crosses the 2nd data downwards
It does need to look into the current time index (0) and the previous time index (-1) of both the 1t and 2nd data

Formula:
diff = data - data1
upcross = last_non_zero_diff < 0 and data0(0) > data1(0)
downcross = last_non_zero_diff > 0 and data0(0) < data1(0)
crossover = upcross - downcross


### 相關網站
-   https://www.investopedia.com/terms/g/goldencross.asp
-   http://finance.yahoo.com/
-   https://backtrader.com/docu/
-   https://backtrader.com/docu/indautoref/#crossover
-   
