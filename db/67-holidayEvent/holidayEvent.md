<p>The store you're working for has decided to organize a special holiday event: every <code>4<sup>th</sup></code> purchase made during this event grants the lucky person who made it a special prize.</p>
<p>All purchases made during the event are stored in the database table <strong>purchases</strong> with the following structure:</p>
<ul>
<li><code>timestamp</code>: unique purchase timestamp;</li>
<li><code>buyer_name</code>: the name of the person who made this purchase.</li>
</ul>
<p>Given the <strong>purchases</strong> table, compose the resulting table with one column <code>winners</code> containing the names of the buyers who won the special prize by making a purchase number <code>k * 4</code> for some integer <code>k</code>. The numbering of the purchases starts with <code>1</code>.<br />
Note, that each person can get no more than one prize (i.e. their name can occur in the answer at most once).<br />
The table should be sorted by the winners' names in <em>ascending</em> order.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For the following table <strong>purchases</strong></p>
<table>
<tr>
<th>timestamp</th>
<th>buyer_name</th>
</tr>
<tr>
<td>2014-11-09 15:23:05</td>
<td>Frank West</td>
</tr>
<tr>
<td>2014-11-09 20:11:02</td>
<td>Terrence Alexander</td>
</tr>
<tr>
<td>2014-11-10 12:10:00</td>
<td>Sandy Cohen</td>
</tr>
<tr>
<td>2014-11-10 13:00:11</td>
<td>Frank West</td>
</tr>
<tr>
<td>2014-11-10 14:09:10</td>
<td>Sandy Cohen</td>
</tr>
<tr>
<td>2014-11-10 14:15:15</td>
<td>Leonard Grant</td>
</tr>
<tr>
<td>2014-11-10 17:09:10</td>
<td>Frank West</td>
</tr>
<tr>
<td>2014-11-10 19:09:10</td>
<td>Diane Tucker</td>
</tr>
<tr>
<td>2014-11-11 18:09:11</td>
<td>Pauline Ross</td>
</tr>
<tr>
<td>2014-11-11 20:00:00</td>
<td>Jasmine Gibson</td>
</tr>
<tr>
<td>2014-11-12 10:12:00</td>
<td>Kim Neal</td>
</tr>
<tr>
<td>2014-11-12 10:12:01</td>
<td>Frank West</td>
</tr>
<tr>
<td>2014-11-12 15:14:42</td>
<td>Sean Kim</td>
</tr>
</table>
<p>the output should be</p>
<table>
<tr>
<th>winners</th>
</tr>
<tr>
<td>Diane Tucker</td>
</tr>
<tr>
<td>Frank West</td>
</tr>
</table>
<p>because Frank West made the <code>4<sup>th</sup></code> and the <code>12<sup>th</sup></code> purchases, and Diane Tucker's purchase was the <code>8<sup>th</sup></code>.</p>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
