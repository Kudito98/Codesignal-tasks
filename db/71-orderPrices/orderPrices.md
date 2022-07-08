<p>You're writing queries for the database of an online store.</p>
<p>You were given access to the <strong>orders</strong> and <strong>item_prices</strong> tables, which have the following structures:</p>
<ul>
<li><strong>orders</strong>:
<ul>
<li><code>id</code>: the unique order ID;</li>
<li><code>buyer</code>: the buyer's name;</li>
<li><code>items</code>: the ID of the items included in the order, separated by a semicolon <code>;</code>. Contains at least one ID.</li>
</ul>
</li>
<li><strong>item_prices</strong>:
<ul>
<li><code>id</code>: the unique item ID;</li>
<li><code>price</code>: the price of the item.</li>
</ul>
</li>
</ul>
<p>Given the <strong>orders</strong> and <strong>item_prices</strong> tables, write a function that will calculate each order's total price, given the purchased <code>items</code> as a string of item IDs separated by semicolons.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>The following tables <strong>orders</strong></p>
<table>
<tr>
<th>id</th>
<th>buyer</th>
<th>items</th>
</tr>
<tr>
  <td>1</td>
  <td>Justin Penrose</td>
  <td>1</td>
</tr>
<tr>
  <td>2</td>
  <td>Bertha Neiman</td>
  <td>1;2;14</td>
</tr>
<tr>
  <td>3</td>
  <td>John Doe</td>
  <td>1;14;15</td>
</tr>
</table>
<p>and <strong>item_prices</strong></p>
<table>
<tr>
<th>id</th>
<th>price</th>
</tr>
<tr>
  <td>1</td>
  <td>100</td>
</tr>
<tr>
  <td>2</td>
  <td>200</td>
</tr>
<tr>
  <td>3</td>
  <td>500</td>
</tr>
<tr>
  <td>4</td>
  <td>250</td>
</tr>
<tr>
  <td>14</td>
  <td>50</td>
</tr>
<tr>
  <td>15</td>
  <td>75</td>
</tr>
<tr>
  <td>16</td>
  <td>100</td>
</tr>
</table>
<p>the output should be</p>
<table>
<tr>
<th>id</th>
<th>buyer</th>
<th>total_price</th>
</tr>
<tr>
  <td>1</td>
  <td>Justin Penrose</td>
  <td>100</td>
</tr>
<tr>
  <td>2</td>
  <td>Bertha Neiman</td>
  <td>350</td>
</tr>
<tr>
  <td>3</td>
  <td>John Doe</td>
  <td>225</td>
</tr>
</table>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
