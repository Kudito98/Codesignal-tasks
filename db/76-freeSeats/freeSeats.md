<p>You're working on the tech support team of an airline company, and your boss has asked you to implement a feature that shows the number of available seats on every flight.</p>
<p>Information about the airline is stored in three tables - <strong>flights</strong>, <strong>planes</strong>, and <strong>purchases</strong>, respectively. The tables are structured as follows:</p>
<ul>
<li><strong>flights</strong>:
<ul>
<li><code>flight_id</code>: the unique flight id;</li>
<li><code>plane_id</code>: the id of the plane making the flight.</li>
</ul>
</li>
<li><strong>planes</strong>:
<ul>
<li><code>plane_id</code>: the unique plane id;</li>
<li><code>number_of_seats</code>: the number of seats on the plane.</li>
</ul>
</li>
<li><strong>purchases</strong>:
<ul>
<li><code>flight_id</code>: the flight id of the purchase;</li>
<li><code>seat_no</code>: the seat number of the purchase.</li>
</ul>
</li>
</ul>
<p>It is guaranteed that in the <strong>purchases</strong> table, the pairs <code>(flight_id, seat_no)</code> are unique.</p>
<p>With the information provided in the database, you need to calculate the number of seats that are not yet purchased for each <code>flight_id</code>.</p>
<p>Given tables <strong>flights</strong>, <strong>planes</strong>, and <strong>purchases</strong>, write a stored procedure that returns a rowset as follows: The resulting rowset should have columns <code>flight_id</code> and <code>free_seats</code>, where for each <code>flight_id</code>, <code>free_seats</code> is the number of seats that have not been purchased yet. The rows of the rowset should be ordered by <code>flight_id</code> in ascending order. It is guaranteed that the information in table <strong>purchases</strong> is consistent and there are no purchases for non-existing <code>flight_id</code>s or <code>seat_no</code>s.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For the following tables <strong>flights</strong></p>
<table>
  <tr>
    <th>flight_id</th>
    <th>plane_id</th>
  </tr>
  <tr>
    <td>111</td>
    <td>128</td>
  </tr>
  <tr>
    <td>87</td>
    <td>157</td>
  </tr>
  <tr>
    <td>100</td>
    <td>23</td>
  </tr>
  <tr>
    <td>121</td>
    <td>23</td>
  </tr>
</table>
<p><strong>planes</strong></p>
<table>
<tr>
<th>plane_id</th>
<th>number_of_seats</th>
</tr>
<tr>
<td>128</td>
<td>5</td>
</tr>
<tr>
<td>23</td>
<td>7</td>
</tr>
<tr>
<td>157</td>
<td>4</td>
</tr>
<tr>
<td>239</td>
<td>2</td>
</tr>
</table>
<p>and <strong>purchases</strong></p>
<table>
<tr>
<th>flight_id</th>
<th>seat_no</th>
</tr>
<tr>
<td>111</td>
<td>1</td>
</tr>
<tr>
<td>87</td>
<td>1</td>
</tr>
<tr>
<td>87</td>
<td>7</td>
</tr>
<tr>
<td>100</td>
<td>5</td>
</tr>
</table>
<p>the output should be</p>
<table>
<tr>
<th>flight_id</th>
<th>free_seats</th>
</tr>
<tr>
<td>87</td>
<td>2</td>
</tr>
<tr>
<td>100</td>
<td>6</td>
</tr>
<tr>
<td>111</td>
<td>4</td>
</tr>
<tr>
<td>121</td>
<td>7</td>
</tr>
</table>
<ul>
<li>Flight number <code>87</code> has <code>4</code> seats, and <code>2</code> of them have been purchased;</li>
<li>Flight number <code>100</code> has <code>7</code> seats, and one of them has been purchased;</li>
<li>Flight number <code>111</code> has <code>5</code> seats, and one of them has been purchased;</li>
<li>Flight number <code>121</code> has <code>7</code> seats, and none of them have been purchased.</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">MySQL hint</span></p>
<p>To return a row set in a MySQL stored procedure, the last statement in the stored procedure should be a <em>SELECT</em> statement, followed by a semi-colon.<br />
E.g.</p>
<pre><code>CREATE PROCEDURE freeSeats()
BEGIN
        SELECT * FROM planes;
END
</code></pre>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
