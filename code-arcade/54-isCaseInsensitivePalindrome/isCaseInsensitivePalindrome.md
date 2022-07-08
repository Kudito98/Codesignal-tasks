<p>Given a string, check if it can become a <a href="keyword://palindrome" target="_blank">palindrome</a> through a case change of some (possibly, none) letters.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>inputString = "AaBaa"</code>, the output should be<br />
<code>solution(inputString) = true</code>.</p>
<p><code>"aabaa"</code> is a palindrome as well as <code>"AABAA"</code>, <code>"aaBaa"</code>, etc.</p>
</li>
<li>
<p>For <code>inputString = "abac"</code>, the output should be<br />
<code>solution(inputString) = false</code>.</p>
<p>All the strings which can be obtained via changing case of some group of letters, i.e. <code>"abac"</code>, <code>"Abac"</code>, <code>"aBAc"</code> and 13 more, are not palindromes.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string inputString</strong></p>
<p>Non-empty string consisting of English letters.</p>
<p><em>Guaranteed constraints:</em><br />
<code>4 ≤ inputString.length ≤ 10</code>.</p>
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
