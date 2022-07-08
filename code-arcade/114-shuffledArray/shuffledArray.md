<p>A noob programmer was given two simple tasks: sum and sort the elements of the given array<br />
<code>a = [a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>]</code>. He started with summing and did it easily, but decided to store the sum he found in some random position of the original array which was a bad idea. Now he needs to cope with the second task, sorting the original array <code>a</code>, and it's giving him trouble since he modified it.</p>
<p>Given the array <code>shuffled</code>, consisting of elements <code>a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>, a<sub>1</sub> + a<sub>2</sub> + ... + a<sub>n</sub></code> in random order, return the sorted array of original elements <code>a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub></code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>shuffled = [1, 12, 3, 6, 2]</code>, the output should be<br />
<code>solution(shuffled) = [1, 2, 3, 6]</code>.</p>
<p><code>1 + 3 + 6 + 2 = 12</code>, which means that <code>1</code>, <code>3</code>, <code>6</code> and <code>2</code> are original elements of the array.</p>
</li>
<li>
<p>For <code>shuffled = [1, -3, -5, 7, 2]</code>, the output should be<br />
<code>solution(shuffled) = [-5, -3, 2, 7]</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer shuffled</strong></p>
<p>Array of at least two integers. It is guaranteed that there is an index <code>i</code> such that <code>shuffled[i] = shuffled[0] + ... + shuffled[i - 1] + shuffled[i + 1] + ... + shuffled[n]</code>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ shuffled.length ≤ 10<sup>4</sup></code>,<br />
<code>-5 · 10<sup>4</sup> ≤ shuffled[i] ≤ 5 · 10<sup>4</sup></code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>A sorted array of <code>shuffled.length - 1</code> elements.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
