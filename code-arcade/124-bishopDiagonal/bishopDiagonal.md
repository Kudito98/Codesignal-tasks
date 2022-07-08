<p>In the Land Of Chess, bishops don't really like each other. In fact, when two bishops happen to stand on the <em>same diagonal</em>, they immediately rush towards the opposite ends of that same diagonal.</p>
<p>Given the initial positions (in chess notation) of two bishops, <code>bishop1</code> and <code>bishop2</code>, calculate their future positions. Keep in mind that bishops won't move unless they see each other along the same diagonal.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>bishop1 = "d7"</code> and <code>bishop2 = "f5"</code>, the output should be<br />
<code>solution(bishop1, bishop2) = ["c8", "h3"]</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/bishopDiagonal/img/ex_1.jpg?_tm=1624426129186" alt /></p>
</li>
<li>
<p>For <code>bishop1 = "d8"</code> and <code>bishop2 = "b5"</code>, the output should be<br />
<code>solution(bishop1, bishop2) = ["b5", "d8"]</code>.</p>
<p>The bishops don't belong to the same diagonal, so they don't move.<br />
<img src="https://codesignal.s3.amazonaws.com/tasks/bishopDiagonal/img/ex_2.jpg?_tm=1624426129403" alt /></p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string bishop1</strong></p>
<p>Coordinates of the first bishop in <a href="keyword://chess-notation" target="_blank">chess notation</a>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>bishop1.length = 2</code>,<br />
<code>'a' ≤ bishop1[0] ≤ 'h'</code>,<br />
<code>1 ≤ bishop1[1] ≤ 8</code>.</p>
</li>
<li>
<p><strong>[input] string bishop2</strong></p>
<p>Coordinates of the second bishop in the same notation.</p>
<p><em>Guaranteed constraints:</em><br />
<code>bishop2.length = 2</code>,<br />
<code>'a' ≤ bishop2[0] ≤ 'h'</code>,<br />
<code>1 ≤ bishop2[1] ≤ 8</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>Coordinates of the bishops in <a href="keyword://lexicographical-order-for-strings" target="_blank">lexicographical order</a> after they check the diagonals they stand on.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
