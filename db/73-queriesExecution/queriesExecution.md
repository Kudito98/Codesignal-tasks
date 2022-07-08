<p>You're working at a company that sells handmade toys. You're supposed to write a monthly report for your managers about how the company is doing. It takes a lot of time to create these reports manually, so you decided to write a function that will make the process easier.</p>
<p>Information for your reports is given in three tables:</p>
<ul>
<li><strong>orders</strong> (information about the orders made throughout the month):
<ul>
<li><code>order_id</code>: the unique order ID;</li>
<li><code>order_type</code>: either <code>"Buy"</code> or <code>"Sell"</code>;</li>
<li><code>date_placed</code>: the date the order was made;</li>
<li><code>order_qty</code>: the quantity of ordered items;</li>
<li><code>order_price</code>: the price of the order;</li>
</ul>
</li>
<li><strong>execution</strong> (information about executed orders):
<ul>
<li><code>execution_id</code>: the unique execution ID;</li>
<li><code>order_id</code>: foreign key referencing <code>orders.order_id</code>;</li>
<li><code>execution_date</code>: the date of the execution;</li>
<li><code>execution_qty</code>: the quantity of bought or sold items;</li>
<li><code>execution_price</code>: the cost of the execution;</li>
</ul>
</li>
<li><strong>queries</strong> (queries which results should be in the reports):
<ul>
<li><code>query_name</code>: the name of the query;</li>
<li><code>code</code>: the code of the query that should be executed; it's guaranteed that each <code>code</code> returns exactly one value.</li>
</ul>
</li>
</ul>
<p>In order to prepare the required values for your next report, you should create a new table with columns <code>query_name</code> and <code>val</code>. For each <code>query_name</code>, the result of the executed query should be stored in the respective <code>val</code> column. The table should be sorted by <code>query_name</code> in ascending order.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For the following tables <strong>orders</strong>:</p>
<table>
  <tr>
    <th>order_id</th>
    <th>order_type</th>
    <th>date_placed</th>
    <th>order_qty</th>
    <th>order_price</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Buy</td>
    <td>2014-03-15</td>
    <td>5</td>
    <td>50</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Buy</td>
    <td>2014-02-03</td>
    <td>15</td>
    <td>23</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Sell</td>
    <td>2014-01-16</td>
    <td>45</td>
    <td>2</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Sell</td>
    <td>2014-01-17</td>
    <td>10</td>
    <td>7</td>
  </tr>
</table>
<p><strong>execution</strong>:</p>
<table>
  <tr>
    <th>execution_id</th>
    <th>order_id</th>
    <th>execution_date</th>
    <th>execution_qty</th>
    <th>execution_price</th>
  </tr>
  <tr>
    <td>1</td>
    <td>1</td>
    <td>2014-03-16</td>
    <td>2</td>
    <td>49</td>
  </tr>
  <tr>
    <td>2</td>
    <td>1</td>
    <td>2014-03-17</td>
    <td>3</td>
    <td>51</td>
  </tr>
  <tr>
    <td>3</td>
    <td>2</td>
    <td>2014-02-03</td>
    <td>15</td>
    <td>22</td>
  </tr>
  <tr>
    <td>4</td>
    <td>3</td>
    <td>2014-01-17</td>
    <td>45</td>
    <td>2</td>
  </tr>
</table>
<p>and <strong>queries</strong>:</p>
<table>
<tr>
<th>query_name</th>
<th>code</th>
</tr>
<tr>
  <td>AVG_EXEC_PRICE</td>
  <td>SELECT AVG(execution_price) FROM `execution`</td>
</tr>
<tr>
  <td>COUNT_EXECUTIONS</td>
  <td>SELECT COUNT(execution_id) FROM `execution`</td>
</tr>
<tr>
  <td>MIN_ORDER_DATE</td>
  <td>SELECT MIN(date_placed) FROM `orders`</td>
</tr>
<tr>
  <td>SUM_ORD_QTY</td>
  <td>SELECT SUM(order_qty) FROM `orders`</td>
</tr>
</table>
the output should be
<table>
<tr>
<th>query_name</th>
<th>val</th>
</tr>
<tr>
  <td>AVG_EXEC_PRICE</td>
  <td>31.000000000</td>
</tr>
<tr>
  <td>COUNT_EXECUTIONS</td>
  <td>4</td>
</tr>
<tr>
  <td>MIN_ORDER_DATE</td>
  <td>2014-01-16</td>
</tr>
<tr>
  <td>SUM_ORD_QTY</td>
  <td>75</td>
</tr>
</table>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
