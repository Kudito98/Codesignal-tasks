<p>Your task is to imitate a turn-based variation of the popular "Snake" game.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/snakeGame/img/snake.gif?_tm=1624666387111" alt /></p>
<p>You are given the initial configuration of the board and a list of commands which the snake follows one-by-one. The game ends if one of the following happens:</p>
<ul>
<li>the snake tries to eat its tail;</li>
<li>the snake tries to move out of the board;</li>
<li>it executes all the given commands.</li>
</ul>
<p>Output the board configuration after the game ends.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>For</li>
</ul>
<pre><code>gameBoard = [['.', '.', '.', '.'],
             ['.', '.', '&lt;', '*'],
             ['.', '.', '.', '*']]
</code></pre>
<p>and <code>commands = "FFFFFRFFRRLLF"</code>, the output should be</p>
<pre><code>solution(gameBoard, commands) = [['.', '.', '.', '.'],
                                  ['X', 'X', 'X', '.'],
                                  ['.', '.', '.', '.']]
</code></pre>
<ul>
<li>For</li>
</ul>
<pre><code>gameBoard = [['.', '.', '^', '.', '.'],
             ['.', '.', '*', '*', '.'],
             ['.', '.', '.', '*', '*']]
</code></pre>
<p>and <code>commands = "RFRF"</code>, the output should be</p>
<pre><code>solution(gameBoard, commands) = [['.', '.', 'X', 'X', '.'],
                                  ['.', '.', 'X', 'X', '.'],
                                  ['.', '.', '.', 'X', '.']]
</code></pre>
<ul>
<li>For</li>
</ul>
<pre><code>gameBoard = [['.', '.', '*', '&gt;', '.'],
             ['.', '*', '*', '.', '.'],
             ['.', '.', '.', '.', '.']]
</code></pre>
<p>and <code>commands = "FRFFRFFRFLFF"</code>, the output should be</p>
<pre><code>solution(gameBoard, commands) = [['.', '.', '.', '.', '.'],
                                  ['&lt;', '*', '*', '.', '.'],
                                  ['.', '.', '*', '.', '.']]
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.char gameBoard</strong></p>
<p>A rectangular matrix of characters. It is guaranteed that it represents a correct game board configuration, i.e. there is exactly one snake. Direction of snake's head is depicted by one of the following characters (<code>'^'</code>, <code>'&gt;'</code>, <code>'v'</code>, <code>'&lt;'</code>). All of the other snake's body parts are depicted by <code>'*'</code>s (note, that if the snake has length <code>1</code> then there is no asterisks in its representation). All cells which are not occupied by the snake are depicted by <code>'.'</code>s.</p>
<p>It is guaranteed that <strong>all snake cells are connected</strong> and <strong>no snake cell has more than two neighbors</strong>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ gameBoard.length ≤ 10</code>,<br />
<code>1 ≤ gameBoard[0].length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] string commands</strong></p>
<p>A list of commands, where <code>'F'</code> means go one cell forward in the current direction, <code>'L'</code> and <code>'R'</code> mean change current direction <code>90</code> degrees left (counter-clockwise) or right (clockwise) correspondingly.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ commands.length ≤ 40</code>.</p>
</li>
<li>
<p><strong>[output] array.array.char</strong></p>
<p>Configuration of the board after the end of the game.</p>
<p>If the snake dies, output its state before the losing move and replace each of the cells it occupied with <code>X</code>s.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
