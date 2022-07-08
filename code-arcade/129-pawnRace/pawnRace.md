<p><em>Pawn race</em> is a game for two people, played on an ordinary <code>8 × 8</code> chessboard. The first player has a white pawn, the second one - a black pawn. Initially the pawns are placed somewhere on the board so that the <code>1<sup>st</sup></code> and the <code>8<sup>th</sup></code> rows are not occupied. Players take turns to make a move.</p>
<p>White pawn moves upwards, black one moves downwards. The following moves are allowed:</p>
<ul>
<li>one-cell move on the same vertical in the allowed direction;</li>
<li>two-cell move on the same vertical in the allowed direction, if the pawn is standing on the <code>2<sup>nd</sup></code> (for the white pawn) or the <code>7<sup>th</sup></code> (for the black pawn) row. Note that even with the two-cell move a pawn can't jump over the opponent's pawn;</li>
<li>capture move one cell forward in the allowed direction and one cell to the left or to the right.</li>
</ul>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/pawnRace/img/move_types.png?_tm=1624100951784" alt /></p>
<p>The purpose of the game is to reach the the 1<sup>st</sup> row (for the black pawn) or the 8<sup>th</sup> row (for the white one), or to capture the opponent's pawn.</p>
<p>Given the initial positions and whose turn it is, determine who will win or declare it a draw (i.e. it is impossible for any player to win). Assume that the players play optimally.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>For <code>white = "e2"</code>, <code>black = "e7"</code>, and <code>toMove = 'w'</code>, the output should be<br />
<code>solution(white, black, toMove) = "draw"</code>;</li>
<li>For <code>white = "e3"</code>, <code>black = "d7"</code>, and <code>toMove = 'b'</code>, the output should be<br />
<code>solution(white, black, toMove) = "black"</code>;</li>
<li>For <code>white = "a7"</code>, <code>black = "h2"</code>, and <code>toMove = 'w'</code>, the output should be<br />
<code>solution(white, black, toMove) = "white"</code>.</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string white</strong></p>
<p>Coordinates of the white pawn in the <a href="keyword://chess-notation" target="_blank">chess notation</a>.</p>
</li>
<li>
<p><strong>[input] string black</strong></p>
<p>Position of the black pawn in the same notation. It is guaranteed that <code>white ≠ black</code>.</p>
</li>
<li>
<p><strong>[input] char toMove</strong></p>
<p><code>'w'</code> if it is the first player's turn, <code>'b'</code> otherwise.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p><code>"white"</code>, <code>"black"</code> or <code>"draw"</code> depending on the result of the game.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
