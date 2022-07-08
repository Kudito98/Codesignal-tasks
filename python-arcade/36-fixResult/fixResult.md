<p>Your teacher asked you to implement a function that calculates the Answer to the Ultimate Question of Life, the Universe, and Everything and returns it as an array of integers. After several hours of hardcore coding you managed to write such a function, and it produced a quite reasonable <code>result</code>. However, when you decided to compare your answer with results of your classmates, you discovered that the elements of your <code>result</code> are roughly <code>10</code> times greater than the ones your peers got.</p>
<p>You don't have time to investigate the problem, so you need to implement a function that will fix the given array for you. Given <code>result</code>, return an array of the same length, where the <code>i<sup>th</sup></code> element is equal to the <code>i<sup>th</sup></code> element of <code>result</code> with the last digit dropped.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>result = [42, 239, 365, 50]</code>, the output should be<br />
<code>solution(result) = [4, 23, 36, 5]</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer result</strong></p>
<p>The result your function produced, where each element is greater than <code>9</code>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ result.length ≤ 15</code>,<br />
<code>10 ≤ result[i] ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>Array consisting of elements of <code>result</code> with last digits dropped.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
