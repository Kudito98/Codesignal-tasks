<p>Several people are standing in a row and need to be divided into two teams. The first person goes into <em>team 1</em>, the second goes into <em>team 2</em>, the third goes into <em>team 1</em> again, the fourth into <em>team 2</em>, and so on.</p>
<p>You are given an array of positive integers - the weights of the people. Return an array of two integers, where the first element is the total weight of <em>team 1</em>, and the second element is the total weight of <em>team 2</em> after the division is complete.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>a = [50, 60, 60, 45, 70]</code>, the output should be<br />
<code>solution(a) = [180, 105]</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer a</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ a.length ≤ 10<sup>5</sup></code>,<br />
<code>45 ≤ a[i] ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
