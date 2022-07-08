<p>A <em>ciphertext alphabet</em> is obtained from the <a href="keyword://plaintext-alphabet" target="_blank">plaintext alphabet</a> by means of rearranging some characters. For example <code>"bacdef...xyz"</code> will be a simple ciphertext alphabet where <code>a</code> and <code>b</code> are rearranged.</p>
<p>A <em>substitution cipher</em> is a method of encoding where each letter of the <em>plaintext alphabet</em> is replaced with the corresponding (i.e. having the same index) letter of some <em>ciphertext alphabet</em>.</p>
<p>Given two strings, check whether it is possible to obtain them from each other using some (possibly, different) <em>substitution ciphers</em>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>string1 = "aacb"</code> and <code>string2 = "aabc"</code>, the output should be<br />
<code>solution(string1, string2) = true</code>.</p>
<p>Any <em>ciphertext alphabet</em> that starts with <code>acb...</code> would make this transformation possible.</p>
</li>
<li>
<p>For <code>string1 = "aa"</code> and <code>string2 = "bc"</code>, the output should be<br />
<code>solution(string1, string2) = false</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string string1</strong></p>
<p>A string consisting of lowercase English characters.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ string1.length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] string string2</strong></p>
<p>A string consisting of lowercase English characters of the same length as <code>string1</code>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>string2.length = string1.length</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
