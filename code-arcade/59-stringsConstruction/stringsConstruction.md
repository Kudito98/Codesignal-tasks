<p>Given two strings <code>a</code> and <code>b</code>, both consisting only of lowercase English letters, your task is to calculate how many strings equal to <code>a</code> can be constructed using only letters from the string <code>b</code>? Each letter can be used only once and in one string only.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>a = "abc"</code> and <code>b = "abccba"</code>, the output should be <code>solution(a, b) = 2</code>.</p>
<p>We can construct <code>2</code> strings <code>a = "abc"</code> using only letters from the string <code>b</code>.</p>
</li>
<li>
<p>For <code>a = "ab"</code> and <code>b = "abcbcb"</code>, the output should be <code>solution(a, b) = 1</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string a</strong></p>
<p>String to construct, containing only lowercase English letters.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ a.length ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[input] string b</strong></p>
<p>String containing needed letters, containing only lowercase English letters.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ b.length ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number of strings <code>a</code> that can be constructed from the string <code>b</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
