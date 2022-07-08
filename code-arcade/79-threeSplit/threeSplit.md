<p>You have a long strip of paper with integers written on it in a single line from left to right. You wish to cut the paper into exactly three pieces such that each piece contains at least one integer and the sum of the integers in each piece is the same. You cannot cut through a number, i.e. each initial number will unambiguously belong to one of the pieces after cutting. How many ways can you do it?</p>
<p>It is guaranteed that the sum of all elements in the array is divisible by <code>3</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>a = [0, -1, 0, -1, 0, -1]</code>, the output should be<br />
<code>solution(a) = 4</code>.</p>
<p>Here are all possible ways:</p>
<ul>
<li><code>[0, -1] [0, -1] [0, -1]</code></li>
<li><code>[0, -1] [0, -1, 0] [-1]</code></li>
<li><code>[0, -1, 0] [-1, 0] [-1]</code></li>
<li><code>[0, -1, 0] [-1] [0, -1]</code></li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer a</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>5 ≤ a.length ≤ 10<sup>4</sup></code>,<br />
<code>-10<sup>8</sup> ≤ a[i] ≤ 10<sup>8</sup></code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>It's guaranteed that for the given test cases the answer always fits signed <code>32</code>-bit integer type.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
