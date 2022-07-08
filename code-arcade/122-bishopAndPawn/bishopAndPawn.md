<p>Given the positions of a white <code>bishop</code> and a black <code>pawn</code> on the standard chess board, determine whether the bishop can capture the pawn in one move.</p>
<p>The bishop has no restrictions in distance for each move, but is limited to diagonal movement. Check out the example below to see how it can move:<br />
<img src="https://codesignal.s3.amazonaws.com/tasks/bishopAndPawn/img/bishop.jpg?_tm=1624426127191" alt /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>bishop = "a1"</code> and <code>pawn = "c3"</code>, the output should be<br />
<code>solution(bishop, pawn) = true</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/bishopAndPawn/img/ex1.jpg?_tm=1624426127437" alt /></p>
</li>
<li>
<p>For <code>bishop = "h1"</code> and <code>pawn = "h3"</code>, the output should be<br />
<code>solution(bishop, pawn) = false</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/bishopAndPawn/img/ex2.jpg?_tm=1624426127674" alt /></p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string bishop</strong></p>
<p>Coordinates of the white bishop in the <a href="keyword://chess-notation" target="_blank">chess notation</a>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>bishop.length = 2</code>,<br />
<code>'a' ≤ bishop[0] ≤ 'h'</code>,<br />
<code>1 ≤ bishop[1] ≤ 8</code>.</p>
</li>
<li>
<p><strong>[input] string pawn</strong></p>
<p>Coordinates of the black pawn in the same notation.</p>
<p><em>Guaranteed constraints:</em><br />
<code>pawn.length = 2</code>,<br />
<code>'a' ≤ pawn[0] ≤ 'h'</code>,<br />
<code>1 ≤ pawn[1] ≤ 8</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the bishop can capture the pawn, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
