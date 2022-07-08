<p>Given a positive integer number and a certain length, we need to modify the given number to have a specified length. We are allowed to do that either by cutting out leading digits (if the number needs to be shortened) or by adding <code>0s</code> in front of the original number.</p>
<p><strong>Example</strong></p>
<ul>
<li>For <code>number = 1234</code> and <code>width = 2</code>, the output should be<br />
<code>solution(number, width) = "34"</code>;</li>
<li>For <code>number = 1234</code> and <code>width = 4</code>, the output should be<br />
<code>solution(number, width) = "1234"</code>;</li>
<li>For <code>number = 1234</code> and <code>width = 5</code>, the output should be<br />
<code>solution(number, width) = "01234"</code>.</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer number</strong></p>
<p>A non-negative integer.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ number ≤ 10<sup>9</sup></code>.</p>
</li>
<li>
<p><strong>[input] integer width</strong></p>
<p>A positive integer representing the desired length.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ width ≤ 50</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>The modified version of <code>number</code> as described above.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
