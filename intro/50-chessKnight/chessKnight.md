<p>Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.</p>
<p>The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/chessKnight/img/knight.jpg?_tm=1624642282452" alt /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>cell = "a1"</code>, the output should be<br />
<code>solution(cell) = 2</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/chessKnight/img/ex_1.jpg?_tm=1624642282672" alt /></p>
</li>
<li>
<p>For <code>cell = "c2"</code>, the output should be<br />
<code>solution(cell) = 6</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/chessKnight/img/ex_2.jpg?_tm=1624642282948" alt /></p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string cell</strong></p>
<p>String consisting of 2 letters - coordinates of the knight on an <code>8 × 8</code> chessboard in <a href="keyword://chess-notation" target="_blank">chess notation</a>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>cell.length = 2</code>,<br />
<code>'a' ≤ cell[0] ≤ 'h'</code>,<br />
<code>1 ≤ cell[1] ≤ 8</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
