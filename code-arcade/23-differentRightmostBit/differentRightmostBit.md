<p>You're given two integers, <code>n</code> and <code>m</code>. Find position of the rightmost bit in which they differ in their binary representations (it is guaranteed that such a bit exists), counting from right to left.</p>
<p>Return the value of <code>2<sup>position_of_the_found_bit</sup></code> (0-based).</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>n = 11</code> and <code>m = 13</code>, the output should be<br />
<code>solution(n, m) = 2</code>.</p>
<p><code>11<sub>10</sub> = 10<b><font color="red">1</font></b>1<sub>2</sub></code>, <code>13<sub>10</sub> = 11<b><font color="red">0</font></b>1<sub>2</sub></code>, the rightmost bit in which they differ is the bit at position <code>1</code> (0-based) from the right in the binary representations.<br />
So the answer is <code>2<sup>1</sup> = 2</code>.</p>
</li>
<li>
<p>For <code>n = 7</code> and <code>m = 23</code>, the output should be<br />
<code>solution(n, m) = 16</code>.</p>
<p><code>7<sub>10</sub> = 111<sub>2</sub></code>, <code>23<sub>10</sub> = 10111<sub>2</sub></code>, i.e.</p>
<pre><code>00111
10111
</code></pre>
<p>So the answer is <code>2<sup>4</sup> = 16</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ n ≤ 2<sup>30</sup></code>.</p>
</li>
<li>
<p><strong>[input] integer m</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ m ≤ 2<sup>30</sup></code>,<br />
<code>n ≠ m</code>.</p>
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
