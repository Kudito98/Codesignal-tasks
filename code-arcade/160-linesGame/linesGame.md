<p>Let's remember the '90s and play an old-school <em>Lines</em> game with the following rules.</p>
<p>The game starts with a <code>9 × 9</code> field with several colored balls placed on its cells (there are 7 possible colors but not all colors have to be present initially). The player can move one ball per turn, and they may only move a ball if there is a clear path between the current position of the chosen ball and the desired destination. Clear paths are formed by neighboring empty cells. Two cells are neighboring if they have a common side. The goal is to remove balls by forming lines (horizontal, vertical or diagonal) of at least five balls of the same color. If the player manages to form one or more such lines, the move is called <em>successful</em>, and the balls in those lines disappear. Otherwise, the move is called <em>unsuccessful</em>, and three more balls appear on the field.</p>
<p>You are given the game logs, and your task is to calculate the player's final score. Here's the information you have:</p>
<ul>
<li>The <code>field</code> state at the initial moment;</li>
<li>The <code>clicks</code> the user has made. Note that a click does not necessarily result in a move:
<ul>
<li>If the user clicks a ball and then another, the first click is ignored;</li>
<li>If two consecutive clicks result in an incorrect move, they are ignored;</li>
</ul>
</li>
<li>After each <em>unsuccessful</em> move three more balls appear:
<ul>
<li><code>newBalls</code> contains the balls' colors;</li>
<li><code>newBallsCoordinates</code> contains their coordinates;</li>
<li>Note that after the balls appear, new lines may form;</li>
</ul>
</li>
<li><em>Whenever</em> new lines appear, they are removed and the player receives <code>A + B - 1</code> points, where:
<ul>
<li><code>A</code> is the number of lines of at least five balls;</li>
<li><code>B</code> is the total number of balls in those lines;</li>
</ul>
</li>
<li>Possible ball colors are <em>red</em>, <em>blue</em>, <em>orange</em>, <em>violet</em>, <em>green</em>, <em>yellow</em> and <em>cyan</em>, which are represented in logs by<br />
<code>"R"</code>, <code>"B"</code>, <code>"O"</code>, <code>"V"</code>, <code>"G"</code>, <code>"Y"</code> and <code>"C"</code> respectively.</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For</p>
<pre><code>field = [['.', 'G', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', 'V', '.'],
         ['.', 'O', '.', '.', 'O', '.', '.', '.', '.'],
         ['.', '.', '.', '.', 'O', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', 'O'],
         ['.', '.', '.', '.', 'O', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['R', '.', '.', '.', '.', '.', '.', 'B', 'R'],
         ['.', '.', 'C', '.', '.', '.', '.', 'Y', 'O']]
</code></pre>
<p><code>clicks = [[4, 8], [2, 1], [4, 4], [6, 4], [4, 8], [1, 2], [1, 4], [4, 8], [6, 4]]</code>,<br />
<code>newBalls = ['R', 'V', 'C', 'G', 'Y', 'O']</code>, and<br />
<code>newBallsCoordinates = [[1, 2], [8, 5], [8, 6], [1, 1], [1, 8], [7, 4]]</code>, the output should be<br />
<code>solution(field, clicks, newBalls, newBallsCoordinates) = 6</code>.</p>
<p>The only correct moves were:</p>
<ul>
<li>Orange ball moved from <code>[2, 1]</code> to <code>[4, 4]</code>;</li>
<li>Red ball moved from <code>[1, 2]</code> to <code>[1, 4]</code>;</li>
<li>Orange ball moved from <code>[4, 8]</code> to <code>[6, 4]</code></li>
</ul>
<p>After the third move a vertical line with <code>6</code> orange balls appears, so it is removed and the player receives <code>1 + 6 - 1 = 6</code> points.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/linesGame/img/example1.jpg?_tm=1621896091865" alt /></p>
</li>
<li>
<p>For</p>
<pre><code>field = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', 'O', '.', 'O', '.', 'O', '.', '.'],
         ['.', '.', '.', 'O', 'O', 'O', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', 'O'],
         ['.', '.', '.', 'O', 'O', 'O', '.', '.', '.'],
         ['.', '.', 'O', '.', 'O', '.', 'O', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.']]
</code></pre>
<p><code>clicks = [[4, 8], [4, 4]]</code>,<br />
<code>newBalls = []</code>, and<br />
<code>newBallsCoordinates = []</code>, the output should be<br />
<code>solution(field, clicks, newBalls, newBallsCoordinates) = 17</code>.</p>
<p>After the move there will be three lines with exactly <code>5</code> balls of the same color, so the answer is <code>3 + (5 + 5 + 5) - 1 = 17</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/linesGame/img/example2.jpg?_tm=1621896092270" alt /></p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.char field</strong></p>
<p>A rectangular matrix, where each element represents either a ball of some color (see above), or an empty cell (<code>'.'</code>).<br />
It is guaranteed that initially there are no lines of five or more balls of the same color.</p>
<p><em>Guaranteed constraints:</em><br />
<code>field.length = 9</code>,<br />
<code>field[i].length = 9</code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer clicks</strong></p>
<p>Each element of <code>clicks</code> consists of two integers and represents some cell from <code>fields</code> that was clicked.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ clicks.length ≤ 40</code>,<br />
<code>0 ≤ clicks[i][j] ≤ 8</code>.</p>
</li>
<li>
<p><strong>[input] array.char newBalls</strong></p>
<p>It is guaranteed that there are enough elements in the array to add balls after each <em>unsuccessful</em> move.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ newBalls.length ≤ 60</code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer newBallsCoordinates</strong></p>
<p>The <code>i<sup>th</sup></code> element represents the coordinates of the <code>i<sup>th</sup></code> appeared ball.<br />
It is guaranteed that balls are added only to the empty cells.</p>
<p><em>Guaranteed constraints:</em><br />
<code>newBallsCoordinates.length = newBalls.length</code>,<br />
<code>newBallsCoordinates[i].length = 2</code>,<br />
<code>0 ≤ newBallsCoordinates[i][j] ≤ 8</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The player's final score.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
