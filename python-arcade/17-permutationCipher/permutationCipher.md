<p>You found your very first laptop in the attic, and decided to give in to nostalgia and turn it on. The laptop turned out to be password protected, but you know how to crack it: you have always used the same <code>password</code>, but encrypt it using <em>permutation ciphers</em> with various keys. The <code>key</code> to the cipher used to protect your old laptop very conveniently happened to be written on the laptop lid.</p>
<p>Here's how <em>permutation cipher</em> works: the <code>key</code> to it consists of all the letters of the alphabet written up in some order. All occurrences of letter <code>'a'</code> in the encrypted text are substituted with the first letter of the <code>key</code>, all occurrences of letter <code>'b'</code> are replaced with the second letter from the <code>key</code>, and so on, up to letter <code>'z'</code> replaced with the last symbol of the <code>key</code>.</p>
<p>Given the <code>password</code> you always use, your task is to encrypt it using the <em>permutation cipher</em> with the given <code>key</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>password = "iamthebest"</code> and<br />
<code>key = "zabcdefghijklmnopqrstuvwxy"</code>, the output should be<br />
<code>solution(password, key) = "hzlsgdadrs"</code>.</p>
<p>Here's a table that can be used to encrypt the text:</p>
<pre><code>abcdefghijklmnopqrstuvwxyz
||  |  ||   |     || 
vv  v  vv   v     vv
zabcdefghijklmnopqrstuvwxy
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string password</strong></p>
<p>The password you always use. It is guaranteed to consist only of lowercase English letters.<br />
If you're using Python 2, note that the string is given as a unicode.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ password.length ≤ 26</code>.</p>
</li>
<li>
<p><strong>[input] string key</strong></p>
<p>The key to the <em>permutation cipher</em>. It is guaranteed to be a permutation of the <a href="keyword://plaintext-alphabet" target="_blank">plaintext alphabet</a>.<br />
If you're using Python 2, note that the string is given as a unicode.</p>
<p><em>Guaranteed constraints:</em><br />
<code>key.length = 26</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>Your <code>password</code> encrypted by the <em>permutations cipher</em> with the given <code>key</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
