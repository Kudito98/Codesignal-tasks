<p>Your web application tracks the activities of its users using a tracking system. While a user hasn't logged in or signed up, all the user's actions are tracked using <code>anonymous_id</code> and the <code>user_id</code> is <code>null</code>, and afterwards they are tracked using the same <code>anonymous_id</code> and <code>user_id</code>. It is known that after a user logs in or signs up, the <code>user_id</code> is no longer <code>null</code>.</p>
<p>You are given the table <strong>tracks</strong>, which contains the following columns:</p>
<ul>
<li><code>received_at</code> - the unique timestamp of action;</li>
<li><code>event_name</code> - the name of the action that was performed at this time;</li>
<li><code>anonymous_id</code> - the anonymous ID of user;</li>
<li><code>user_id</code> - the user ID, which can be <code>null</code>.</li>
</ul>
<p>Your task is to find two events for each <code>anonymous_id</code>, which will be the column <code>anonym_id</code> in the returned table. Find the last event where the user was tracked only by <code>anonymous_id</code> (column <code>last_null</code>) and the first event that was tracked by <code>user_id</code> (column <code>first_notnull</code>). The resulting table should be sorted by <code>anonym_id</code>.</p>
<p><strong>Note:</strong> It is not guaranteed that a user ever logs in or signs up. In this case, the column <code>first_notnull</code> should have a value of <code>null</code>. However, it is guaranteed that for each <code>anonymous_id</code>, there is at least one event where <code>user_id</code> equals <code>null</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For given table <strong>tracks</strong></p>
<table>
<tr>
<th>received_at</th>
<th>event_name</th>
<th>anonymous_id</th>
<th>user_id</th>
</tr>
<tr>
<td>2016-01-01 09:13:12</td>
<td>buttonClicked</td>
<td>1</td>
<td>NULL</td>
</tr>
<tr>
<td>2016-01-02 09:14:15</td>
<td>pageReloaded</td>
<td>3</td>
<td>NULL</td>
</tr>
<tr>
<td>2016-02-02 10:15:13</td>
<td>pageRendered</td>
<td>2</td>
<td>NULL</td>
</tr>
<tr>
<td>2016-02-03 10:15:23</td>
<td>commentWritten</td>
<td>3</td>
<td>NULL</td>
</tr>
<tr>
<td>2016-03-03 11:15:15</td>
<td>avatarUpdated</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td>2016-03-04 11:15:24</td>
<td>statusUpdated</td>
<td>1</td>
<td>1</td>
</tr>
</table>
<p>the output should be</p>
<table>
<tr>
<th>anonym_id</th>
<th>last_null</th>
<th>first_notnull</th>
</tr>
<tr>
<td>1</td>
<td>buttonClicked</td>
<td>statusUpdated</td>
</tr>
<tr>
<td>2</td>
<td>pageRendered</td>
<td>avatarUpdated</td>
</tr>
<tr>
<td>3</td>
<td>commentWritten</td>
<td>NULL</td>
</tr>
</table>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
