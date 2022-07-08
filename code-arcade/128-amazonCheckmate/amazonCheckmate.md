<p>An <em>amazon</em> (also known as a <em>queen + knight compound</em>) is an imaginary chess piece that can move like a queen or a knight (or, equivalently, like a rook, bishop, or knight). The diagram below shows all squares which the amazon can attack from <code>e4</code> (circles represent knight-like moves while crosses correspond to queen-like moves).</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/amazonCheckmate/img/amazon.png?_tm=1624426060032" alt /></p>
<p>Recently, you've come across a diagram with only three pieces left on the board: a white <em>amazon</em>, the white king, and the black king. It's black's move. You don't have time to determine whether the game is over or not, but you'd like to figure it out in your head. Unfortunately, the diagram is smudged and you can't see the position of the black king, so you'll need to consider all possible positions.</p>
<p>Given the positions of the white pieces on a standard chessboard (using algebraic notation), your task is to determine the number of possible black king's positions such that:</p>
<ul>
<li>it's checkmate (i.e. black's king is under the <em>amazon's</em> attack and it cannot make a valid move);</li>
<li>it's check (i.e. black's king is under the <em>amazon's</em> attack but it can reach a safe square in one move);</li>
<li>it's stalemate (i.e. black's king is on a safe square but it cannot make a valid move);</li>
<li>black's king is on a safe square and it can make a valid move.</li>
</ul>
<p>Note that two kings cannot be placed on two adjacent squares (including two diagonally adjacent ones).</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>king = "d3"</code> and <code>amazon = "e4"</code>, the output should be<br />
<code>solution(king, amazon) = [5, 21, 0, 29]</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/amazonCheckmate/img/example1.png?_tm=1624426060314" alt /></p>
<p>Red crosses correspond to the checkmate positions, orange pluses refer to check positions, and green circles denote safe squares.</p>
</li>
<li>
<p>For <code>king = "a1"</code> and <code>amazon = "g5"</code>, the output should be<br />
<code>solution(king, amazon) = [0, 29, 1, 29]</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/amazonCheckmate/img/example2.png?_tm=1624426060529" alt /></p>
<p>The stalemate position is marked by a blue square.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string king</strong></p>
<p>The position of the white king, in <a href="keyword://chess-notation" target="_blank">chess notation</a>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>king.length = 2</code>,<br />
<code>'a' ≤ king[0] ≤ 'h'</code>,<br />
<code>1 ≤ king[1] ≤ 8</code>.</p>
</li>
<li>
<p><strong>[input] string amazon</strong></p>
<p>The position of the white <em>amazon</em>, in the same notation.</p>
<p><em>Guaranteed constraints:</em><br />
<code>amazon.length = 2</code>,<br />
<code>'a' ≤ amazon[0] ≤ 'h'</code>,<br />
<code>1 ≤ amazon[1] ≤ 8</code>,<br />
<code>amazon ≠ king</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>An array of four integers, each equal to the number of black's king positions corresponding to a specific situation. More specifically, the array should be of the form <code>[checkmate positions, check positions, stalemate positions, safe positions]</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
