<p>Given two cells on the standard chess board, determine whether they have the same color or not.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>cell1 = "A1"</code> and <code>cell2 = "C3"</code>, the output should be<br />
<code>solution(cell1, cell2) = true</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/chessBoardCellColor/img/example1.png?_tm=1624649616776" alt /></p>
</li>
<li>
<p>For <code>cell1 = "A1"</code> and <code>cell2 = "H3"</code>, the output should be<br />
<code>solution(cell1, cell2) = false</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/chessBoardCellColor/img/example2.png?_tm=1624649617010" alt /></p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string cell1</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>cell1.length = 2</code>,<br />
<code>'A' ≤ cell1[0] ≤ 'H'</code>,<br />
<code>1 ≤ cell1[1] ≤ 8</code>.</p>
</li>
<li>
<p><strong>[input] string cell2</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>cell2.length = 2</code>,<br />
<code>'A' ≤ cell2[0] ≤ 'H'</code>,<br />
<code>1 ≤ cell2[1] ≤ 8</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if both cells have the same color, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
