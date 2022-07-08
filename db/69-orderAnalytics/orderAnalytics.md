<p>You're working in a big delivery company that has to handle a lot of orders.</p>
<p>The information about all orders is stored in the table <strong>orders</strong>. Here is its structure:</p>
<ul>
<li><code>id</code>: unique order id;</li>
<li><code>order_date</code>: order date (having <code>DATE</code> type) in the format <code>YYYY-MM-DD</code>;</li>
<li><code>type</code>: the type of the product in the order;</li>
<li><code>quantity</code>: the quantity of the product in the order;</li>
<li><code>price</code>: the price of one item of the product.</li>
</ul>
<p>In order to get a better view of your data you decided to create a new table called <strong>orders_analytics</strong>. It should contain the same orders as the <strong>orders</strong> and consist of the following columns:</p>
<ul>
<li><code>id</code>: order id;</li>
<li><code>year</code>: the year of the order;</li>
<li><code>quarter</code>: the <em>quarter</em> of the year in which the order was taken;</li>
<li><code>type</code>: the type of the product in the order;</li>
<li><code>total_price</code>: the total price of the order (<code>total_price = price * quantity</code>).</li>
</ul>
<p>The <em>quarter</em> of the year is defined as follows:</p>
<ul>
<li>01 January till 31 March refers to the <code>1<sup>st</sup></code> quarter;</li>
<li>01 April till 30 June refers to the <code>2<sup>nd</sup></code> quarter;</li>
<li>01 July till 30 September refers to the <code>3<sup>rd</sup></code> quarter;</li>
<li>01 October till 31 December refers to the <code>4<sup>th</sup></code> quarter.</li>
</ul>
<p>Given the table <strong>orders</strong>, build the new table <strong>order_analytics</strong> and print all its rows ordered by order <code>id</code>s.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For the following table <strong>orders</strong></p>
<table>
  <tr>
    <th>id</th>
    <th>order_date</th>
    <th>type</th>
    <th>quantity</th>
    <th>price</th>
  </tr>
  <tr>
    <td>1</td>
    <td>2015-08-15</td>
    <td>Pizza</td>
    <td>2</td>
    <td>25</td>
  </tr>
  <tr>
    <td>2</td>
    <td>2016-05-11</td>
    <td>Sushi</td>
    <td>1</td>
    <td>37</td>
  </tr>
  <tr>
    <td>3</td>
    <td>2015-01-01</td>
    <td>Wok</td>
    <td>5</td>
    <td>8</td>
  </tr>
  <tr>
    <td>4</td>
    <td>2016-12-31</td>
    <td>Cake</td>
    <td>1</td>
    <td>49</td>
  </tr>
</table>
<p>the output should be</p>
<table>
<tr>
<th>id</th>
<th>year</th>
<th>quarter</th>
<th>type</th>
<th>total_price</th>
</tr>
<tr>
<td>1</td>
<td>2015</td>
<td>3</td>
<td>Pizza</td>
<td>50</td>
</tr>
<tr>
<td>2</td>
<td>2016</td>
<td>2</td>
<td>Sushi</td>
<td>37</td>
</tr>
<tr>
<td>3</td>
<td>2015</td>
<td>1</td>
<td>Wok</td>
<td>40</td>
</tr>
<tr>
<td>4</td>
<td>2016</td>
<td>4</td>
<td>Cake</td>
<td>49</td>
</tr>
</table>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
