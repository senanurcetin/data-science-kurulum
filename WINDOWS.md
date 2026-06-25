# Kurulum Adımları

Başlayalım :rocket:

## Windows için

Başlamadan önce, bilgisayarınızda yüklü olan Windows sürümünün bu kurulum talimatlarıyla uyumlu olup olmadığını kontrol etmemiz gerekiyor.

### Windows 10 veya Windows 11

Bilgisayarınızı kurabilmek için **Windows 10 veya Windows 11** yüklü olması gerekir.

Eğer Windows 11 kullanıyorsanız, hazırsınız.

Eğer Windows 10 kullanıyorsanız, versiyon numarasının 2004 ve üzeri olması gerekir. Eğer 2004 öncesi ise önce update etmelisiniz.


## Virtualization

Bilgisayarınızın BIOS’unda Virtualization seçeneklerinin etkinleştirildiğinden emin olmamız gerekiyor.

Çoğu bilgisayarda böyledir. Ama kontrol edelim:
- `Windows` + `R` kombinasyonunu tuşlayın
- `taskmgr` yazın
- `Enter` tuşuna basın
- `Performance` sekmesini açın
- `CPU`yu seçin

![](images/windows_task_manager.png)

:heavy_check_mark: Eğer resimdeki gibi "Virtualization: Enabled" görüyorsanız hazırsınız dmektir ve sonraki adımlarla devam edebilirsiniz.

:x: Aksi durumda slack'te **Data-Yardım** kanalından yardım isteyebilirsiniz.



## Windows Subsystem for Linux (WSL)

WSL, Ubuntu’yu çalıştırmak için kullandığımız development environment’tır. WSL hakkında daha fazla bilgiyi [buradan](https://docs.microsoft.com/en-us/windows/wsl/faq) edinebilirsiniz.


WSL 2 ve Ubuntu’yu tek bir komutla **Windows Command Prompt** üzerinden kuracağız.

:warning: Aşağıdaki talimatta, **Windows Command Prompt**’u yalnızca `Ok`’e tıklayarak ya da `Enter`’a basarak değil, **administrator yetkileriyle** çalıştırmak için `Ctrl` + `Shift` + `Enter` tuş kombinasyonuna dikkat edin.

- `Windows` + `R` tuşlarına basın
- `cmd` yazın
- **`Ctrl` + `Shift` + `Enter`** tuşlarına basın

:warning: Yetki yükseltme ile ilgili UAC onayını kabul etmeniz gerekebilir.

Siyah bir terminal penceresi açılacaktır:

- Aşağıdaki komutu kopyalayın (`Ctrl` + `C`)
- Terminal penceresine yapıştırın (`Ctrl` + `V` veya pencereye sağ tıklayarak)
- `Enter` tuşuna basarak çalıştırın

```powershell
wsl --install
```

:heavy_check_mark: Eğer hata almadı iseniz bilgisayarınızı restart edin ve sonraki adımlarla devam edin :+1:

:x: Aksi durumda slack'te **Data-Yardım** kanalından yardım isteyebilirsiniz.


## Ubuntu

### Yükleme

After restarting you computer, you should see a terminal window saying WSL is resuming the Ubuntu installation process. When it's done, Ubuntu will be launched.

### İlk çalıştırma

İlk çalıştırmada sizden bazı bilgiler istenecektir:

* Bir **username** seçin:

  * tek kelime
  * küçük harf
  * özel karakter yok
  * örneğin: `wit` veya adınız
* Bir **password** seçin
* Password’ünüzü onaylayın

:warning: Password’ünüzü yazarken ekranda hiçbir şey görünmeyecektir, **bu normaldir**. Bu, yalnızca password’ünüzün kendisini değil, aynı zamanda uzunluğunu da gizleyen bir güvenlik özelliğidir. Sadece password’ünüzü yazın ve bitirdiğinizde `Enter` tuşuna basın.


### Ubuntu'daki WSL versiyonunu kontrol edin

- `Windows` + `R` kombinasyonunu tuşlayın
- `cmd` yazın
- `Enter` tuşuna basın

Aşağıdaki komutu çalıştırın :

```bash
wsl -l -v
```

:heavy_check_mark: Ubuntu WSL sürümü 2 ise, hazırsınız :+1:

:x: Ubuntu WSL sürümü 1 ise, bunu sürüm 2’ye dönüştürmemiz gerekecek.

<details>
  <summary>WSL V1'i V2'ye dönüştürme</summary>

  Command Prompt pencersinde aşağıdaki komutu çalıştırın :

  ```bash
  wsl --set-version Ubuntu 2
  ```

  :heavy_check_mark: Birkaç saniye sonra şu mesajı görmelisiniz: `The conversion is complete`.

  :x: Eğer çalışmazsa, Ubuntu dosyalarının sıkıştırılmamış olduğundan emin olmamız gerekir.


<details>
  <summary> Ubuntu dosyalarının sıkıştırılmış mı kontrolü</summary>

  - `Windows` + `R` tuşlarına basın
  - `%localappdata%\Packages` yazın
  - `Enter` tuşuna basın
  - `CanonicalGroupLimited.UbuntuonWindows...` adlı klasörü açın
  - `LocalState` klasörüne sağ tıklayın
  - `Properties`’e tıklayın
  - `Advanced`’e tıklayın
  - `Compress content` seçeneğinin **işaretli olmadığından** emin olun, ardından `Ok`’e tıklayın

  Değişiklikleri **yalnızca bu klasöre** uygulayın ve Ubuntu WSL sürümünü tekrar dönüştürmeyi deneyin.

  :x: Sorun devam ediyorsa slack'te **Data-Yardım** kanalından yardım isteyebilirsiniz.

</details>

Terminali kapatabilirsiniz.

</details>

### Check your username

Ubuntu terminalinde aşağıdaki kodu çalıştırın :

```bash
whoami
```

Kullanıcı adınızı size göstermeli.

:x: Eğer `root` olarak görünüyorsa **Data-Yardım** kanalından yardım isteyebilirsiniz.


## Visual Studio Code

### Yükleme

[Visual Studio Code](https://code.visualstudio.com) text editor'ünü yükleyin.

- [Visual Studio Code download sayfasını](https://code.visualstudio.com/download) açın.
- "Windows"u seçin
- İndirdiğiniz dosyayı çalıştırın
- Aşağıdaki ayarları seçin:

![](images/windows_vscode_installation.png)

Yükleme bitince VS Code'u çalıştırın.

### VS Code'u Ubuntu'ya bağlama

VS Code’un Ubuntu ile doğru şekilde etkileşim kurabilmesi için [Remote - WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) VS Code extension’ını yükleyelim.

**Ubuntu terminal**’ini açın.

Aşağıdaki komutları terminale kopyalayıp yapıştırın:


```bash
code --install-extension ms-vscode-remote.remote-wsl
```

Şimdi terminalden VS Code'u açmayı deneyelim:

```bash
code .
```

:heavy_check_mark: VS Code penceresinin sol alt köşesinde `WSL: Ubuntu` ifadesini görüyorsanız, hazırsınız :+1:

![](images/windows_remote_wsl.png)

:x: Aksi durumda slack'te **Data-Yardım** kanalından yardım isteyebilirsiniz.



## Windows Terminal

### Yükleme

:information_source: Aşağıdaki talimatlar Windows sürümünüze bağlıdır.

Windows 11 kullanıyorsanız, Windows Terminal zaten yüklüdür ve bir sonraki bölüme geçebilirsiniz :point_down:

Windows 10 kullanıyorsanız, modern ve gelişmiş bir terminal olan Windows Terminal’i yükleyelim.


<details>
<summary><strong>Windows 10</strong>: Windows Terminal Yükleme</summary>

- `Start`’a tıklayın
- `Microsoft Store` yazın
- Listeden `Microsoft Store`’a tıklayın
- Arama çubuğunda `Windows Terminal` aratın
- **`Windows Terminal`’i seçin**
- `Install`’a tıklayın

:warning: **Windows Terminal Preview**’u **yüklemeyin**, yalnızca **Windows Terminal**’i yükleyin!

<details>
  <summary>Yanlış Windows Terminal'i yükledi isen. uninstall etme adımları</summary>

  Yanlış bir Windows Terminal sürümünü kaldırmak için Windows 10’un **Installed Program List** bölümüne gitmeniz yeterlidir:

  - `Windows` + `R` tuşlarına basın
  - `ms-settings:appsfeatures` yazın
  - `Enter` tuşuna basın

  Kaldırmak istediğiniz yazılımı bulun ve **uninstall** düğmesine tıklayın.

</details>

Kurulum tamamlandığında `Install` düğmesi `Launch` düğmesine dönüşür; buna tıklayın.

</details>

### Ubuntu'yu default terminal yapma

Ubuntu’yu Windows Terminal uygulamanızın varsayılan terminali yapalım.

`Ctrl` + `,` tuşlarına basın.

Bu, terminal ayarlarını açacaktır:

![](images/windows_terminal_settings.png)

- Varsayılan profili **“Ubuntu”** olarak değiştirin
- **“Save”**’e tıklayın
- **“Open JSON file”**’a tıklayın

Ubuntu logosu olarak bir penguen yerine turuncu bir daire görebilirsiniz.

Değiştirmeniz gereken kısmı kırmızıyla daire içine aldık:

![](images/windows_terminal_settings_json.png)

Öncelikle Ubuntu’nun, Windows dizini yerine doğrudan **Ubuntu Home Directory** içinde başlamasını sağlayalım:

- Hem `"name": "Ubuntu",` hem de `"hidden": false,` içeren girdiyi bulun
- Bunun hemen altına aşağıdaki satırı ekleyin:


```bash
"commandline": "wsl.exe ~",
```

:warning: Satırın sonundaki virgülü unutmayın!

Ardından, Windows ile Ubuntu arasında komutları kopyalayıp yapıştırırken çıkan uyarıları devre dışı bırakalım:

- `"defaultProfile": "{2c4de342-...}"` satırını bulun
- Bunun hemen altına aşağıdaki satırı ekleyin:


```bash
"warning.multiLinePaste": false,
```

:warning: Satırın sonundaki virgülü unutmayın!

Bu değişiklikleri `Ctrl` + `S` tuşlarına basarak kaydedebilirsiniz.

:heavy_check_mark: **Windows Terminal** artık kurulmuş durumda :+1:

Bu terminal sekmeleri destekler; mevcut sekmenin yanındaki **+** işaretine tıklayarak yeni bir terminal sekmesi açabilirsiniz.

**Bundan sonra terminal veya konsoldan bahsettiğimizde, kastedilen her zaman bu terminal olacaktır.** Artık başka bir terminal **KULLANMAYIN**.



## VS Code Eklentileri

### Yükleme

Bazı yararlı eklentileri VS Code uygulamamıza yükleyelim.

```bash
code --install-extension ms-vscode.sublime-keybindings
code --install-extension emmanuelbeziat.vscode-great-icons
code --install-extension MS-vsliveshare.vsliveshare
code --install-extension ms-python.python
code --install-extension KevinRose.vsc-python-indent
code --install-extension ms-python.vscode-pylance
code --install-extension ms-toolsai.jupyter
code --install-extension alexcvzz.vscode-sqlite
```

Neler yükledik? kendi sayfalarına bir göz atabilirsiniz:
- [Sublime Text Keymap and Settings Importer](https://marketplace.visualstudio.com/items?itemName=ms-vscode.sublime-keybindings)
- [VSCode Great Icons](https://marketplace.visualstudio.com/items?itemName=emmanuelbeziat.vscode-great-icons)
- [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Python Indent](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite)


## Komut Satırı Araçları

### locale kontrolü

Locale, programları dilinize ve ülkenize göre özelleştirmenizi sağlayan bir mekanizmadır.

Varsayılan locale’in İngilizce olarak ayarlandığını doğrulayalım; lütfen Ubuntu terminalinde şunu yazın:

```bash
locale
```

Çıktı `LANG=en_US.UTF-8` içermiyorsa, İngilizce locale’i yüklemek için Ubuntu terminalinde aşağıdaki komutu çalıştırın:

```bash
sudo locale-gen en_US.UTF-8
```

Eğer bundan sonra terminalinizde şu uyarıyı alırsanız (`bash: warning: setlocale: LC_ALL: cannot change locale (en_US.utf-8)`), lütfen aşağıdakileri yapın:

<details>
  <summary>locale oluşturma</summary>

Aşağıdaki satırları terminalde çalıştırın.

```bash
sudo update-locale LANG=en_US.UTF8
sudo apt-get update
sudo apt-get install language-pack-en language-pack-en-base manpages
```
</details>

### Zsh & Git

Varsayılan `bash` [shell](https://en.wikipedia.org/wiki/Shell_%28computing%29) yerine `zsh` kullanacağız.

Ayrıca, version control için kullanılan bir command line yazılımı olan [`git`](https://git-scm.com/)’i de kullanacağız.

Bunları, diğer faydalı araçlarla birlikte yükleyelim:

* Bir **Ubuntu terminali** açın
* Aşağıdaki komutları kopyalayıp yapıştırın


```bash
sudo apt update
```

```bash
sudo apt install -y curl git imagemagick jq unzip vim zsh tree
```

Bu komutlar sizden parolanızı isteyecektir; parolanızı yazın.

:warning: Parolanızı yazarken ekranda hiçbir şey görünmeyecektir, **bu normaldir**. Bu, yalnızca parolanın kendisini değil, aynı zamanda uzunluğunu da gizleyen bir güvenlik özelliğidir. Parolanızı yazın ve bitirdiğinizde `Enter` tuşuna basın.


### GitHub CLI Yüklemesi

Şimdi [GitHub resmi CLI](https://cli.github.com) (Command Line Interface)’i yükleyelim. Bu, command line üzerinden GitHub hesabınızla etkileşim kurmak için kullanılan bir yazılımdır.

Terminalinizde aşağıdaki komutları kopyalayıp yapıştırın ve istenirse parolanızı yazın:

```bash
sudo apt remove -y gitsome
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
```

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
```

```bash
sudo apt update
```

```bash
sudo apt install -y gh
```

`gh`’nin bilgisayarınıza başarıyla yüklendiğini kontrol etmek için şunu çalıştırabilirsiniz:

```bash
gh --version
```

:heavy_check_mark: `gh version X.Y.Z (YYYY-MM-DD)` gibi bir ifade çıktı ise her şey hazır demektir.:+1:

:x: Aksi durumda slack'te **Data-Yardım** kanalından yardım isteyebilirsiniz.


## Oh-my-zsh

`zsh` plugin'ini yükleyelim: [Oh My Zsh](https://ohmyz.sh/).

Terminal'de aşağıdaki komutu çalıştırın :

```bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

"Do you want to change your default shell to zsh?" sorusu gelince `Y` tuşuna basın.

Kurulum bitince aşağıdaki gibi bir ekran ile karşılaşacaksınız:

![](images/oh_my_zsh.png)


:heavy_check_mark: Benzer bir ekran görüyorsanız, her şey yolunda demektir. Diğer adımlarla devam edebilirsiniz. :+1:

:x: Aksi durumda slack'te **Data-Yardım** kanalından yardım isteyebilirsiniz.



## Default tarayıcınızı Ubuntu'ya bağlayalım

Ubuntu terminalinizden Windows’ta yüklü tarayıcınızla etkileşim kurabildiğinizden emin olmak için, onu burada varsayılan tarayıcı olarak ayarlamamız gerekiyor.

Aşağıdaki komutu çalıştırın ve talimatları izleyin. Araç, sisteminizde mevcut olan tarayıcılardan birini seçmenizi isteyecektir. Tarayıcının önünde gösterilen **numarayı** yazmanız yeterlidir.


```bash
bash -c "$(curl -s https://raw.githubusercontent.com/julesvanrie/wslsetbrowser/refs/heads/main/wslsetbrowser.sh)"
```

Terminali resetleyin:

```bash
exec zsh
```

Ardından, aşağıdaki komutun `"Tarayıcı tanımlandı 👌"` sonucunu döndürdüğünden emin olun:

```bash
[ -z "$BROWSER" ] && echo "ERROR: BROWSER environment variable tanımlaması yapın ⚠️" || echo "Tarayıcı tanımlandı 👌"
```

:x: Hata alırsanız slack'te **Data-Yardım** kanalından yardım isteyebilirsiniz.


## direnv

[direnv](https://direnv.net/) bir shell extension’dır. Proje bazında environment variable’larla çalışmayı kolaylaştırır. Bu, kodunuzun davranışını özelleştirmek için faydalı olacak.

``` bash
sudo apt-get update; sudo apt-get install direnv
echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc
```



## GitHub CLI

CLI [Command-line Interface](https://en.wikipedia.org/wiki/Command-line_interface)'in kısaltmasıdır.

Bu bölümde, GitHub ile doğrudan terminal üzerinden etkileşim kurmak için [GitHub CLI](https://cli.github.com/) kullanacağız.

Önceki adımlar sayesinde bilgisayarınızda zaten yüklenmiş olması gerekir.

GitHub’a SSH kullanarak bağlanmak için GitHub CLI (`gh`) kullanacağız. SSH, bilinen kullanıcı adı/parola ikilisi yerine SSH key’leri kullanarak giriş yapmayı sağlayan bir protokoldür.

İlk olarak **login** olmak için, aşağıdaki komutu terminalinize kopyalayıp yapıştırın:

:warning: **Dikkat: `email` kelimesini değiştiremeyin!!!**

```bash
gh auth login -s 'user:email' -w --git-protocol ssh
```

`gh` size bazı sorular soracak :

- `Generate a new SSH key to add to your GitHub account?` sorulunca `Enter`'a basın. Sizin için SSH key oluşturacak.

  Eğer zaten SSH key’leriniz varsa, bunun yerine `Upload your SSH public key to your GitHub account?` mesajını göreceksin. Ok tuşlarıyla public key dosya yolunu seçin ve `Enter` tuşuna basın.

- `Enter a passphrase for your new SSH key (Optional)`: Hatırlayabileceğiniz bir parola yazın. Bu, hard drive’ınızda saklanan private key’i korumak için kullanılan bir paroladır. Ardından `Enter` tuşuna basın.

- `Title for your SSH key`. "GitHub CLI" olarak bırakabilirsin, `Enter` tuşuna basın.

Aşağıdakine benzer bir çıktı alacaksın :

```bash
! First copy your one-time code: 0EF9-D015
- Press Enter to open github.com in your browser...
```

Ekrandaki kodu kopyalayın ve yapıştırın (Bu örnek çıktıda kod:`0EF9-D015`), sonra `Enter` tuşuna basın.

Tarayıcınız açılacak ve GitHub CLI’nin GitHub hesabınızı kullanmasına izin vermenizi isteyecektir. Kabul edin ve biraz bekleyin.

Ardından terminale geri dönün, tekrar `Enter` tuşuna basın ve işlem tamamdır.

Doğru şekilde bağlandığınızı kontrol etmek için şunu yazın:

```bash
gh auth status
```

:heavy_check_mark: `Logged in to github.com as <YOUR USERNAME> ` mesajını alıyorsak her şey yolunda demektir ve sonraki adımlarla ilerleyebiliriz :+1:

:x: Aksi durumda slack'te **Data-Yardım** kanalından yardım isteyebilirsiniz.


## Dotfiles

Bazı uygulamalarımızın configuration dosyalarını değiştirerek özel ayarlarımızı yükleyelim. Bunun için dotfile'ları güncelleyeceğiz.

> Dotfiles, Unix tabanlı işletim sistemlerinde kullanıcıların konfigürasyon ayarlarını saklamaya yarayan gizli dosyalardır.

dotfile'ları yükleyelim:

```bash
cd ~/code/$GITHUB_USERNAME/data-science-kurulum/dotfiles && zsh install.sh
```

Şimdi de sanal ortamımız için git ayarlarını güncelleyelim:

```bash
cd ~/code/$GITHUB_USERNAME/data-science-kurulum/dotfiles && zsh git_setup.sh
```

☝️ Bu işlem sizden adınızı (**Adınız Soyadınız**) ve e-posta adresinizi isteyecektir.

:x: Aksi durumda slack'te **Data-Yardım** kanalından yardım isteyebilirsiniz.

Şimdi terminal'i quit edelim.


## SSH passphrase prompt'unu iptal etme

Uzak bir repository ile her iletişim kurduğunuzda passphrase sorulmasını istemezsiniz. Bu yüzden `oh my zsh`’e `ssh-agent` plugin’ini eklemeniz gerekiyor:

Öncelikle `.zshrc` dosyasını açın:

```bash
code ~/.zshrc
```

Ardından:

- `plugins=` ile başlayan satırı bulun
- Plugin listesi sonuna `ssh-agent` ekleyin

:heavy_check_mark: `.zshrc` dosyasını `Ctrl` + `S` ile kaydedin ve metin editörünü kapatın.



## Python Yükleme ([`pyenv`](https://github.com/pyenv/pyenv) ile )

### `conda`yı uninstall edin

Python version’ımızı kurmak ve yönetmek için `pyenv` kullandığımızdan, daha önce [Anaconda](https://www.anaconda.com/) yüklediyseniz bilgisayarınızda bulunabilecek başka bir package manager olan [`conda`](https://docs.conda.io/projects/conda/en/latest/)’yı kaldırmamız gerekiyor. Böylece ileride oluşabilecek olası Python version sorunlarını önlemiş oluruz.

Bilgisayarınızda `conda` yüklü olup olmadığını kontrol edin:

```bash
conda list
```

Eğer `zsh: command not found: conda` mesajını alırsanız, conda kaldırma adımını **atlayabilir** ve bir sonraki bölümü geçebilirsin.


### `pyenv` Yüklemesi

Ubuntu, kullanmak istemediğimiz eski bir Python sürümüyle birlikte gelir. Daha önce Python ve Data Science package’larıyla denemeler yapmak için Anaconda ya da başka bir şey yüklemiş olabilirsiniz. Bunların hiçbiri aslında önemli değil; çünkü Python için profesyonel bir kurulum yapacağız ve bu sayede terminalde `python` yazdığınızda hangi version’ı kullanmak istediğinizi dilediğiniz zaman değiştirebileceksiniz.

Önce, aşağıdaki kodu terminalde kullanarak `pyenv` yükleyelim :

```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
exec zsh
```

Python’ı `pyenv` ile oluşturmak için gerekli olan bazı [dependencies](https://github.com/pyenv/pyenv/wiki/common-build-problems#prerequisites)’leri yükleyelim:


```bash
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev sqlite3 libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev \
python3-dev
```

### Python'ı Yükleme

Eğitim boyunca aynı şeyleri yapabilemek için en güncel ve stable(kararlı) Python sürümünü yükleyelim:

```bash
pyenv install 3.12.9
```

Bu biraz zaman alacaktır. Bu çok normal. Bir kahve alıp gelebilirsiniz...

<details>
  <summary>🛠 `pyenv` bulunamadı hatası alırsanız</summary>

`Command 'pyenv' not found` hatasını alırsanız aşağıdaki satırı çalıştırın :

```bash
source ~/.zprofile
```

Sonra python'u tekrar yüklemeyi deneyin :

```bash
pyenv install 3.12.9
```

:x: Hala hata almaya devam ediyorsanız slack'te **Data-Yardım** kanalından yardım isteyebilirsiniz.

</details>
<br>


Bu adım tamamlandığında bu versiyonu default kullanmak istediğimizi  Python **by default**. This is done with:

```bash
pyenv global 3.12.9
exec zsh
```

Çalıştığından emin olmak için `python --version` kodunu çalıştırın. `3.12.9` görüyorsanız, her şey yolunda demektir!

:x: Aksi durumda slack'te **Data-Yardım** kanalından yardım isteyebilirsiniz.

## Python Sanal Ortamı

İlgili Python package’larını yüklemeye başlamadan önce, eğitim için olan kurulumu özel (dedicated) bir virtual environment içine izole edeceğiz. Bunun için `pyenv`nin [`pyenv-virtualenv`](https://github.com/pyenv/pyenv-virtualenv) adlı bir plugin’ini kullanacağız.

### virtualenv kurulumu

Önce plugin'i yükleyelim:

```bash
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
exec zsh
```

Eğitim boyunca kullanacağımız environment'ı oluşturalım :

```bash
pyenv virtualenv 3.12.9 workintech
```

Default virtual environment'ımızı yeni oluşturduğumuz yapalım:

```bash
pyenv global workintech
```

Harika! Ne zaman bir Python package’ı yükleyecek olursak, bunu bu environment içinde yapacağız.


### Python packages

Artık tertemiz bir `workintech` virtual environment’ımız olduğuna göre, içine bazı package’ları yükleme zamanı geldi.

Öncelikle, Python package’larını [pypi.org](https://pypi.org) üzerinden yüklememizi sağlayan araç olan `pip`i güncelleyelim. `workintech` virtualenv’inin aktif olduğu en son terminalde aşağıdakini çalıştırın:

```bash
pip install --upgrade pip
```

Ardından programın ilk haftaları için bazı package’ları yükleyelim:

``` bash
pip install -r https://raw.githubusercontent.com/workintech/data-science-kurulum/master/specs/releases/linux.txt
```


## Jupyter Notebook tweaking

Notebook’larınızda [`details` disclosure elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details) görünümünü iyileştirelim.

Jupyter config dizininizde bir `custom.css`stylesheet’i oluşturmak için aşağıdaki satırları çalıştırın:

```bash
LOCATION=$(jupyter --config-dir)/custom
SOURCE=https://raw.githubusercontent.com/workintech/data-science-kurulum/refs/heads/master/specs/jupyter/custom.css
mkdir -p $LOCATION
curl $SOURCE > $LOCATION/custom.css
```



### Jupyter Notebook’u tarayıcınızda açılacak şekilde yapılandırma

Öncelikle varsayılan tarayıcınızı tekrar yapılandıralım. Bunu daha önce yapmıştık, ancak dotfiles’ı kurduğumuzda bu ayar silindi. Sorun değil, ayarları tekrar yapılandırmak için bu komutu çalıştırın:


```bash
grep -E "export (GH_)*BROWSER" ~/.zshrc.backup >> ~/.zshrc
```

Terminali restart edin :

```bash
exec zsh
```

**Jupyter Notebook** için configuration dosyaları oluşturalım :

``` bash
jupyter notebook --generate-config
```

Şimdi oluşturulan Jupyter configuration dosyasını düzenleyeceğiz:

``` bash
sed -i.backup 's/# c.ServerApp.use_redirect_file = True/c.ServerApp.use_redirect_file = False/' ~/.jupyter/jupyter_notebook_config.py
```

Jupyter'i çalıştıralım:

``` bash
jupyter notebook
```

Yeni bir notebook, yeni bir sekmede açılmalı :

![](images/wsl_jupyter_notebook.png)

Eğer göremiyorsanız ayarlarınızda bir sorun olabilir. Yardım almanız gerekebilir.

Tarayıcınızda notebook pencerelerini kapatarın ve terminalde  `CTRL` + `C` tuş kombinasyonu ile jupyter'i sonlandırın.


## Python Kurulum Kontrolü

### Python ve package kontrolü

terminal'i resetleyelim:

```bash
cd ~/code && exec zsh
```

Python versiyonunu aşağıdaki komut ile kontrol edelim:

```bash
zsh -c "$(curl -fsSL https://raw.githubusercontent.com/workintech/data-science-kurulum/master/checks/python_checker.sh)" 3.12.9
```

Gerekli paketlerin yüklendiğini aşağıdaki komut ile kontrol edelim:
```bash
zsh -c "$(curl -fsSL https://raw.githubusercontent.com/workintech/data-science-kurulum/master/checks/pip_check.sh)"
```

Şimdi, bu paketleri yükleyip yükleyemediğinizi kontrol etmek için aşağıdaki komutu çalıştıralım :

```bash
python -c "$(curl -fsSL https://raw.githubusercontent.com/workintech/data-science-kurulum/master/checks/pip_check.py)"
```

### Jupyter Kontrolü

Jupyter'i çalıştırabildiğimizden emin olalım :

```bash
jupyter notebook
```

Tarayıcımız artık `jupyter`'i yeni bir sekmede açmalı :

![jupyter.png](images/jupyter.png)

`New`e tıkla ve dropdown listesinden `Python 3 (ipykernel)`i seç:

![jupyter_new.png](images/jupyter_new.png)

Yeni bir notebook, yeni bir sekmede açılmalı :

![jupyter_notebook.png](images/jupyter_notebook.png)

Notebook’ta doğru python version’ını çalıştırdığınızdan emin olun. Yeni bir `cell`(hücre) oluşturun ve aşağıdaki kodu çalıştırın :

``` python
import sys; sys.version
```

`3.12.9` çıktısını görmelisiniz. Eğer göremiyorsanız ayarlarınızda bir sorun olabilir. Yardım almanız gerekebilir.

Tarayıcınızda notebook pencerelerini kapatarın ve terminalde  `CTRL` + `C` tuş kombinasyonu ile jupyter'i sonlandırın.

Tebrikler, her şey hazır! Tüm Data Science eğitimi boyunca ihtiyaç duyacağınız tüm third-party package’ları içeren eksiksiz bir python virtual environment kurduk.



## Windows Ayarları

### Windows ve Ubuntu arasında dosya paylaşımı

Windows ile Ubuntu arasında dosya aktarımı yapmanın kolay bir yoluna ihtiyacımız var.

Bunu yapmak için, Windows **File Explorer** içinde Ubuntu dizinlerine kısayollar oluşturalım:

- Windows File Explorer’ı açın (veya `WIN` + `E` kısayolunu kullanın)
- Adres çubuğuna `\\wsl$\` yazın (çalışmazsa `\\wsl$\Ubuntu`)
- Artık Ubuntu dosya sistemine erişiminiz var
- İlgilendiğiniz dizinleri bulmak için Ubuntu dosya sistemi içinde gezinin
- İstediğiniz klasörleri, kısayol oluşturmak için adres çubuğuna sürükleyin


### Ubuntu terminalinden Windows File Explorer’ı açma

Dosyaları taşımak için bir diğer seçenek de Ubuntu terminalinden Windows **File Explorer**’ı açmaktır:

* Bir Ubuntu terminali açın
* İncelemek istediğiniz dizine gidin
* `explorer.exe .` komutunu çalıştırın (alternatif olarak `wslview .` kullanabilirsiniz)
* Bir input/output error mesajı alırsanız, Windows PowerShell’de `wsl --shutdown` komutunu çalıştırın ve ardından bir Ubuntu terminalini yeniden açın




### Ubuntu dosya sisteminde yolunuzu bulma

Ubuntu dosya sistemi içinde bir Windows dizininin tam konumunu ya da bunun tersini bulmak isteyebilirsiniz.

Bir Windows yolunu Ubuntu yoluna veya bir Ubuntu yolunu Windows yoluna dönüştürmek için:

* Bir Ubuntu terminali açın
* Bir Windows yolunu Ubuntu yoluna çevirmek için `wslpath "C:\Program Files"` komutunu kullanın
* Bir Ubuntu yolunu Windows yoluna çevirmek için `wslpath -w "/home"` komutunu kullanın
* Özellikle, `wslpath -w $(pwd)` komutu mevcut Ubuntu dizininizin Windows yolunu döndürür




### Uygulamaları görev çubuğuna sabitleme

Bugün yüklediğiniz uygulamaların çoğunu çok sık kullanacaksınız. Tek tık uzağınızda olmaları için bunları görev çubuğuna sabitleyelim!

Bir uygulamayı görev çubuğuna sabitlemek için uygulamayı açın, görev çubuğundaki simgesine sağ tıklayarak bağlam menüsünü açın ve **“Pin to taskbar”** seçeneğini seçin.

![](images/windows_taskbar.png)

Şunları sabitlemenizi tavsiye ederiz:

* Terminaliniz
* File Explorer
* VS Code
* Internet tarayıcınız
* Slack



## Visual C++ Redistributable

Bazı Python package’ları düzgün çalışabilmek için bir compiler’a ihtiyaç duyar. Haydi bir tane yükleyelim:

[x64 için](https://aka.ms/vs/16/release/vc_redist.x64.exe)
