<p>The latest Tic-Tac-Toe World Championship has just concluded. It was a big success and attracted a lot of participants! Now everyone is waiting for the results. As a member of the judging committee, you've been tasked with creating a championship leaderboard.</p>
<p>The results of all the tic-tac-toe matches are stored in the <strong>results</strong> table, which has the following structure:</p>
<ul>
<li><code>timestamp</code>: the date and time of the game;</li>
<li><code>name_naughts</code>: the name of the player that played with naughts (<code>O</code>);</li>
<li><code>name_crosses</code>: the name of the player that played with crosses (<code>X</code>);</li>
<li><code>board</code>: the state of the tic-tac-toe board at the end of the game, in the format described below.</li>
</ul>
<p>The <code>board</code> is a string of <code>9</code> characters that represent the state of board's <code>9</code> cells at the end of the match. The first <code>3</code> characters represent the first (upper) row, the second <code>3</code> characters represent the second row, etc. The character is <code>O</code> if the respective board cell contained a naught, <code>X</code> if it contained a cross, or <code>.</code> if the cell was empty at the end of the game.</p>
<p>For example, this board</p>
<pre><code> | |O
 |O| 
X|X|X
</code></pre>
<p>is represented by the string <code>..O.O.XXX</code>.</p>
<p>It is guaranteed that the opposing players have different names. It's also guaranteed that each <code>board</code> represents a valid terminal state for a tic-tac-toe game, meaning that either of the players wins or it's a draw.</p>
<p>Players are awarded points based on their performance: They get <code>2</code> points for each game they win, <code>1</code> point for a draw, and <code>0</code> points if they lose.</p>
<p>Create a leaderboard with the following format:</p>
<p>Given the <strong>results</strong> table, compose a results table that has the following six columns: <code>name</code>, <code>points</code>, <code>played</code>, <code>won</code>, <code>draw</code>, and <code>lost</code> , containing the player names, their points calculated as described above, the number of games they have played, the number of games they have won, and the number of games they have lost, respectively. The table should be sorted in descending order by the <code>points</code>, then in ascending order by the total number of <code>played</code> games, then in descending order by the number of victories, and then in ascending order by player <code>name</code>s.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For the following table <strong>results</strong></p>
<table>
<tr>
<th>timestamp</th>
<th>name_naughts</th>
<th>name_crosses</th>
<th>board</th>
</tr>
<tr>
  <td>2017-05-01 08:06:00</td>
  <td>Georgine Greely</td>
  <td>Earnestine Kunzman</td>
  <td>XO.X.OXXO</td>
</tr>
<tr>
  <td>2017-05-01 11:20:00</td>
  <td>Earnestine Kunzman</td>
  <td>Georgine Greely</td>
  <td>.O.OOXXXX</td>
</tr>
<tr>
  <td>2017-05-01 16:48:00</td>
  <td>Renee Fortenberry</td>
  <td>Georgine Greely</td>
  <td>XOOXXO..X</td>
</tr>
<tr>
  <td>2017-05-02 10:57:00</td>
  <td>Renee Fortenberry</td>
  <td>Georgine Greely</td>
  <td>OXXXOOXOX</td>
</tr>
<tr>
  <td>2017-05-03 01:55:00</td>
  <td>Georgine Greely</td>
  <td>Renee Fortenberry</td>
  <td>.X.OX.OX.</td>
</tr>
<tr>
  <td>2017-05-03 04:29:00</td>
  <td>Earnestine Kunzman</td>
  <td>Renee Fortenberry</td>
  <td>OOXXXOXXO</td>
</tr>
<tr>
  <td>2017-05-04 14:29:00</td>
  <td>Renee Fortenberry</td>
  <td>Earnestine Kunzman</td>
  <td>OOX.X.X..</td>
</tr>
<tr>
  <td>2017-05-04 16:00:00</td>
  <td>Earnestine Kunzman</td>
  <td>Renee Fortenberry</td>
  <td>OXOOXXXOX</td>
</tr>
</table>
<p>the output should be</p>
<table>
<tr>
<th>name</th>
<th>points</th>
<th>played</th>
<th>won</th>
<th>draw</th>
<th>lost</th>
</tr>
<tr>
  <td>Renee Fortenberry</td>
  <td>6</td>
  <td>6</td>
  <td>2</td>
  <td>2</td>
  <td>2</td>
</tr>
<tr>
  <td>Earnestine Kunzman</td>
  <td>5</td>
  <td>5</td>
  <td>2</td>
  <td>1</td>
  <td>2</td>
</tr>
<tr>
  <td>Georgine Greely</td>
  <td>5</td>
  <td>5</td>
  <td>2</td>
  <td>1</td>
  <td>2</td>
</tr>
</table>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
