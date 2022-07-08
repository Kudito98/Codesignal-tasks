<p>A pair of numbers is considered to be <em>cool</em> if their product is divisible by their sum. More formally, a pair <code>(i, j)</code> is <em>cool</em> if and only if <code>(i * j) % (i + j) = 0</code>.</p>
<p>Given two lists <code>a</code> and <code>b</code>, find <em>cool</em> pairs with the first number in the pair from <code>a</code>, and the second one from <code>b</code>. Return the number of different sums of elements in such pairs.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>a = [4, 5, 6, 7, 8]</code> and <code>b = [8, 9, 10, 11, 12]</code>,<br />
the output should be<br />
<code>solution(a, b) = 2</code>.</p>
<p>There are three <em>cool</em> pairs that can be formed from these arrays: <code>(4, 12)</code>, <code>(6, 12)</code> and <code>(8, 8)</code>. Their respective sums are <code>16</code>, <code>18</code> and <code>16</code>, which means that there are just <code>2</code> different sums: <code>16</code> and <code>18</code>. Thus, the output should be equal to <code>2</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer a</strong></p>
<p>Array of distinct elements.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ a.length ≤ 100</code>,<br />
<code>1 ≤ a[i] ≤ 100</code>.</p>
</li>
<li>
<p><strong>[input] array.integer b</strong></p>
<p>Array of distinct elements.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ b.length ≤ 100</code>,<br />
<code>1 ≤ b[i] ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number of different sums of elements in <em>cool</em> pairs formed by elements from <code>a</code> and <code>b</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
