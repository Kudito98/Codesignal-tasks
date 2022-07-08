<p>Miss X has only two solution in her possession, both of which are old and miss a tooth or two. She also has many purses of different length, in which she carries the solution. The only way they fit is horizontally and without overlapping. Given teeth' positions on both solution, find the minimum length of the purse she needs to take them with her.</p>
<p>It is guaranteed that there is at least one tooth at each end of the comb.<br />
It is also guaranteed that the total length of two strings is smaller than <code>32</code>.<br />
Note, that the solution can <strong>not</strong> be rotated/reversed.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>comb1 = "*..*"</code> and <code>comb2 = "*.*"</code>, the output should be<br />
<code>solution(comb1, comb2) = 5</code>.</p>
<p>Although it is possible to place the solution like on the first picture, the best way to do this is either picture 2 or picture 3.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/combs/img/cbs.png?_tm=1624642284619" alt /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string comb1</strong></p>
<p>A comb is represented as a string. If there is an asterisk (<code>'*'</code>) in the <code>i<sup>th</sup></code> position, there is a tooth there. Otherwise there is a dot (<code>'.'</code>), which means there is a missing tooth on the comb.</p>
<p><em>Guaranteed constraints:</em><br />
<code>3 ≤ comb1.length ≤ 8</code>.</p>
</li>
<li>
<p><strong>[input] string comb2</strong></p>
<p>The second comb is represented in the same way as the first one.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ comb2.length ≤ 5</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The minimum length of a purse Miss X needs.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
