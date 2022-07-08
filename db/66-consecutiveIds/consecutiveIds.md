<p>You work for an online store in which each item put up for sale gets a unique randomly generated id.</p>
<p>These item ids are stored in the <strong>itemIds</strong> table with only one column:</p>
<ul>
<li><code>id</code>: unique id of an item.</li>
</ul>
<p>However, this system proved to be not very convenient to use in a number of queries that required consecutive ids. To solve this problem, you decided to generate new ids for the items using the following algorithm: the item with the smallest <code>id</code> would get <code>1</code> as a new id, the second smallest would get <code>2</code>, and so on.</p>
<p>Given the <strong>itemIds</strong> table, write a select statement which returns two columns: <code>oldId</code> and <code>newId</code>. The first column should contain the old item id, and the second one should contain the new id generated as described above. The output should be sorted by the <code>newId</code> in <em>ascending</em> order.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For the following table <strong>itemIds</strong></p>
<table><tr>
</tr><tr>
<th>id</th>
</tr>
<td>1</td>

<tr>
<td>12</td>
</tr>
<tr>
<td>23</td>
</tr>
<tr>
<td>42</td>
</tr>
<tr>
<td>49</td>
</tr>
<tr>
<td>678</td>
</tr>
<tr>
<td>3242</td>
</tr>
<tr>
<td>9320</td>
</tr>
<tr>
<td>67867</td>
</tr>
<tr>
<td>84523</td>
</tr>
</table>
<p>the output should be</p>
<table><tr><th>oldId</th><th>newId</th></tr>
<tr>
  <td>1</td>
  <td>1</td>
</tr>
<tr>
  <td>12</td>
  <td>2</td>
</tr>
<tr>
  <td>23</td>
  <td>3</td>
</tr>
<tr>
  <td>42</td>
  <td>4</td>
</tr>
<tr>
  <td>49</td>
  <td>5</td>
</tr>
<tr>
  <td>678</td>
  <td>6</td>
</tr>
<tr>
  <td>3242</td>
  <td>7</td>
</tr>
<tr>
  <td>9320</td>
  <td>8</td>
</tr>
<tr>
  <td>67867</td>
  <td>9</td>
</tr>
<tr>
  <td>84523</td>
  <td>10</td>
</tr>
</table>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
