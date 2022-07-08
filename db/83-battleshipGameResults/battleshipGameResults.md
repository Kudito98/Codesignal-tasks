<p>In the 2-player game Battleship, each player takes turns guessing the position of the other player's battleships on a <code>10 x 10</code> playing board. When a player correctly guesses a grid that contains a segment of an opponent's battleship, the ship is damaged. If all the segments of a ship have been damaged, the ship is declared to be sunk. You're evaluating an ongoing Battleship game, and have two tables.</p>
<p>The table <strong>locations_of_ships</strong> contains the locations of one of the player's ships. This table contains the following columns:</p>
<ul>
<li><code>id</code> - the unique ID of the ship;</li>
<li><code>upper_left_x</code> - the <code>x</code>-coordinate of the upper left corner;</li>
<li><code>upper_left_y</code> - the <code>y</code>-coordinate of the upper left corner;</li>
<li><code>bottom_right_x</code> - the <code>x</code>-coordinate of the bottom right corner;</li>
<li><code>bottom_right_y</code> - the <code>y</code>-coordinate of the bottom right corner.</li>
</ul>
<p>In this task there can be these types of ships - <code>1 × 1, 1 × 2, 1 × 3, 1 × 4, 2 × 1, 3 × 1, 4 × 1 </code>, number of ships of particular type is not fixed, but it is guaranteed that they don't overlap.</p>
<p>The target squares of the opponent's shots are given in another table, <strong>opponents_shots</strong>, which has the following columns:</p>
<ul>
<li><code>id</code> - the unique ID of the shot;</li>
<li><code>target_x</code> - the <code>x</code>-coordinate of the target square;</li>
<li><code>target_y</code> - the <code>y</code>-coordinate of the target square.</li>
</ul>
<p>All the coordinates in these tables are <code>1</code>-based.</p>
<p>The goal is to return a table that describes the current state of the game. For each class of ship (i.e. for each different size), there should be a row containing four integers: a ship's size in the column <code>size</code>, the number of undamaged ships of that type in the column <code>undamaged</code>, the number of partly damaged ships of that size in the column <code>partly_damaged</code>, and the number of ships of that type that have already been sunk in the column <code>sunk</code>. The result should be ordered by the size of the ships.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For given table <strong>locations_of_ships</strong></p>
<table>
<tr>
<th>id</th>
<th>upper_left_x</th>
<th>upper_left_y</th>
<th>bottom_right_x</th>
<th>bottom_right_y</th>
</tr>
<tr>
<td>1</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>1</td>
</tr>
<tr>
<td>2</td>
<td>4</td>
<td>1</td>
<td>4</td>
<td>3</td>
</tr>
<tr>
<td>3</td>
<td>7</td>
<td>1</td>
<td>10</td>
<td>1</td>
</tr>
<tr>
<td>4</td>
<td>10</td>
<td>3</td>
<td>10</td>
<td>4</td>
</tr>
</table>
<p>and table <strong>opponents_shots</strong></p>
<table>
<tr>
<th>id</th>
<th>target_x</th>
<th>target_y</th>
</tr>
<tr>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>2</td>
<td>2</td>
<td>1</td>
</tr>
<tr>
<td>3</td>
<td>4</td>
<td>2</td>
</tr>
</table>
<p>the output should be</p>
<table>
<tr>
<th>size</th>
<th>undamaged</th>
<th>partly_damaged</th>
<th>sunk</th>
</tr>
<tr>
<td>2</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>3</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td>4</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
</table>
<p>The diagram below shows the state of the game board:<br />
<img src="https://codesignal.s3.amazonaws.com/tasks/battleshipGameResults/img/ex.jpg?_tm=1611831910326" alt /></p>
<ul>
<li><strong>[execution time limit] 10 seconds (mysql)</strong></li>
</ul>
