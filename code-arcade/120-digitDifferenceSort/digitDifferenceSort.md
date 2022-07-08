<p>Given an array of integers, sort its elements by the <em>difference</em> of their largest and smallest digits. In the case of a tie, that with the larger index in the array should come first.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>a = [152, 23, 7, 887, 243]</code>, the output should be<br />
<code>solution(a) = [7, 887, 23, 243, 152]</code>.</p>
<p>Here are the <em>differences</em> of all the numbers:</p>
<ul>
<li><code>152</code>: <code>difference = 5 - 1 = 4</code>;</li>
<li><code>23</code>: <code>difference = 3 - 2 = 1</code>;</li>
<li><code>7</code>: <code>difference = 7 - 7 = 0</code>;</li>
<li><code>887</code>: <code>difference = 8 - 7 = 1</code>;</li>
<li><code>243</code>: <code>difference = 4 - 2 = 2</code>.</li>
</ul>
<p><code>23</code> and <code>887</code> have the same <em>difference</em>, but <code>887</code> goes after <code>23</code> in <code>a</code>, so in the sorted array it comes first.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer a</strong></p>
<p>An array of integers.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ sequence.length ≤ 10<sup>4</sup></code>,<br />
<code>1 ≤ sequence[i] ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>Array <code>a</code> sorted as described above.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
