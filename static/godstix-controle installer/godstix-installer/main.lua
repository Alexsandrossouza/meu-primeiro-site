scriptTitle = "GodStix Installer & Update"
scriptAuthor = "Speedy Games Downloads"
scriptVersion = "1.0"
scriptDescription = "Install and update the GodStix plugin for Aurora. v1.0"
scriptIcon = "icon\\icon.xur"
scriptPermissions = { "http", "filesystem", "content" }

require("MenuSystem")
json = require("JSON")

SERVER_URL = "http://stix.speedygamesdownloads.com"
API_BASE = SERVER_URL .. "/api"
gCurrentLang = "pt_br"
gGodStixPath = ""
gDownloadsPath = "Downloads\\"
gAbsoluteDownloadsPath = ""
gShouldExit = false
gLanguageSaved = false

LANGUAGES = {
    { code = "pt_br", name = "Portugues (BR)" },
    { code = "en", name = "English" },
    { code = "es", name = "Espanol" }
}

STRINGS = {
    pt_br = {
        title = "GodStix Installer & Update",
        install_update = "Instalar / Atualizar GodStix",
        changelog = "Changelog",
        settings = "Configuracoes",
        about = "Sobre",
        back = "< Voltar",
        no_network = "Sem Rede",
        no_network_msg = "Seu Xbox nao esta conectado a rede.\n\n1. Verifique o cabo ethernet ou WiFi\n2. Va em Configuracoes do Xbox > Rede\n3. Certifique-se que o roteador esta ligado",
        fetching_releases = "Buscando versoes disponiveis...",
        no_releases = "Nenhuma versao disponivel no momento.",
        select_version = "Selecione a Versao",
        version_list_header = "Escolha uma das versoes abaixo:",
        version_info = "Versao: v%s\nData: %s\nDownloads: %s\n\n%s\n\nDeseja instalar esta versao?",
        version_info_no_desc = "Versao: v%s\nData: %s\nDownloads: %s\n\nDeseja instalar esta versao?",
        version_info_reinstall = "Versao: v%s\nData: %s\nDownloads: %s\n\n%s\n\nEsta versao ja esta instalada.\nDeseja reinstalar esta versao?",
        version_info_reinstall_no_desc = "Versao: v%s\nData: %s\nDownloads: %s\n\nEsta versao ja esta instalada.\nDeseja reinstalar esta versao?",
        downloading = "Baixando GodStix v%s...",
        extracting = "Extraindo arquivos...",
        cleaning = "Removendo versao anterior...",
        preserving_backups = "Preservando backups do usuario...",
        installing = "Instalando GodStix v%s...",
        install_success = "GodStix v%s instalado com sucesso!",
        install_failed = "Falha na instalacao!\n\n%s",
        download_failed = "Falha ao baixar a versao.\n\nVerifique sua conexao e tente novamente.",
        extract_failed = "Falha ao extrair o arquivo baixado.",
        language = "Idioma",
        select_language = "Selecionar Idioma",
        test_connection = "Testar Conexao",
        connection_ok = "Conexao OK!",
        connection_failed = "Falha na conexao com o servidor.",
        about_text = "GodStix Installer & Update v%s\n\nAutor: %s\n\nEste script permite instalar e atualizar\no plugin GodStix para Aurora automaticamente.\n\nSeu backup de WebUI e preservado durante\na atualizacao.",
        confirm_install = "Instalar",
        confirm_reinstall = "Reinstalar",
        cancel = "Cancelar",
        error = "Erro",
        fetch_error = "Erro ao buscar versoes: %s",
        check_self_update = "Verificar Atualizacao do Instalador",
        checking_self_update = "Verificando atualizacao do instalador...",
        self_update_available = "Nova versao do instalador disponivel!\n\nVersao atual: v%s\nNova versao: v%s\n\nDeseja atualizar o instalador?",
        self_update_success = "Instalador atualizado para v%s!",
        self_update_failed = "Falha ao atualizar o instalador.\n\n%s",
        self_update_current = "Seu instalador ja esta na versao mais recente (v%s).",
        self_update_downloading = "Baixando atualizacao do instalador...",
        no_changelog = "Nenhum changelog disponivel para esta versao.",
        changelog_title = "Changelog - v%s"
    },
    en = {
        title = "GodStix Installer & Update",
        install_update = "Install / Update GodStix",
        changelog = "Changelog",
        settings = "Settings",
        about = "About",
        back = "< Back",
        no_network = "No Network",
        no_network_msg = "Your Xbox is not connected to the network.\n\n1. Check ethernet cable or WiFi\n2. Go to Xbox Settings > Network\n3. Make sure the router is on",
        fetching_releases = "Fetching available versions...",
        no_releases = "No versions available at this time.",
        select_version = "Select Version",
        version_list_header = "Choose one of the versions below:",
        version_info = "Version: v%s\nDate: %s\nDownloads: %s\n\n%s\n\nDo you want to install this version?",
        version_info_no_desc = "Version: v%s\nDate: %s\nDownloads: %s\n\nDo you want to install this version?",
        version_info_reinstall = "Version: v%s\nDate: %s\nDownloads: %s\n\n%s\n\nThis version is already installed.\nDo you want to reinstall this version?",
        version_info_reinstall_no_desc = "Version: v%s\nDate: %s\nDownloads: %s\n\nThis version is already installed.\nDo you want to reinstall this version?",
        downloading = "Downloading GodStix v%s...",
        extracting = "Extracting files...",
        cleaning = "Removing previous version...",
        preserving_backups = "Preserving user backups...",
        installing = "Installing GodStix v%s...",
        install_success = "GodStix v%s installed successfully!",
        install_failed = "Installation failed!\n\n%s",
        download_failed = "Failed to download version.\n\nCheck your connection and try again.",
        extract_failed = "Failed to extract downloaded file.",
        language = "Language",
        select_language = "Select Language",
        test_connection = "Test Connection",
        connection_ok = "Connection OK!",
        connection_failed = "Failed to connect to server.",
        about_text = "GodStix Installer & Update v%s\n\nAuthor: %s\n\nThis script lets you install and update\nthe GodStix plugin for Aurora automatically.\n\nYour WebUI backup is preserved during updates.",
        confirm_install = "Install",
        confirm_reinstall = "Reinstall",
        cancel = "Cancel",
        error = "Error",
        fetch_error = "Error fetching versions: %s",
        check_self_update = "Check for Installer Update",
        checking_self_update = "Checking for installer update...",
        self_update_available = "New installer version available!\n\nCurrent version: v%s\nNew version: v%s\n\nDo you want to update the installer?",
        self_update_success = "Installer updated to v%s!",
        self_update_failed = "Failed to update installer.\n\n%s",
        self_update_current = "Your installer is already up to date (v%s).",
        self_update_downloading = "Downloading installer update...",
        no_changelog = "No changelog available for this version.",
        changelog_title = "Changelog - v%s"
    },
    es = {
        title = "GodStix Installer & Update",
        install_update = "Instalar / Actualizar GodStix",
        changelog = "Changelog",
        settings = "Configuracion",
        about = "Acerca de",
        back = "< Volver",
        no_network = "Sin Red",
        no_network_msg = "Tu Xbox no esta conectado a la red.\n\n1. Verifica el cable ethernet o WiFi\n2. Ve a Configuracion de Xbox > Red\n3. Asegurate de que el router este encendido",
        fetching_releases = "Buscando versiones disponibles...",
        no_releases = "No hay versiones disponibles en este momento.",
        select_version = "Seleccionar Version",
        version_list_header = "Elija una de las versiones a continuacion:",
        version_info = "Version: v%s\nFecha: %s\nDescargas: %s\n\n%s\n\nDesea instalar esta version?",
        version_info_no_desc = "Version: v%s\nFecha: %s\nDescargas: %s\n\nDesea instalar esta version?",
        version_info_reinstall = "Version: v%s\nFecha: %s\nDescargas: %s\n\n%s\n\nEsta version ya esta instalada.\nDesea reinstalar esta version?",
        version_info_reinstall_no_desc = "Version: v%s\nFecha: %s\nDescargas: %s\n\nEsta version ya esta instalada.\nDesea reinstalar esta version?",
        downloading = "Descargando GodStix v%s...",
        extracting = "Extrayendo archivos...",
        cleaning = "Eliminando version anterior...",
        preserving_backups = "Preservando copias de seguridad...",
        installing = "Instalando GodStix v%s...",
        install_success = "GodStix v%s instalado exitosamente!",
        install_failed = "Fallo en la instalacion!\n\n%s",
        download_failed = "Error al descargar la version.\n\nVerifique su conexion e intente nuevamente.",
        extract_failed = "Error al extraer el archivo descargado.",
        language = "Idioma",
        select_language = "Seleccionar Idioma",
        test_connection = "Probar Conexion",
        connection_ok = "Conexion OK!",
        connection_failed = "Fallo al conectar con el servidor.",
        about_text = "GodStix Installer & Update v%s\n\nAutor: %s\n\nEste script permite instalar y actualizar\nel plugin GodStix para Aurora automaticamente.\n\nSu copia de WebUI se preserva durante\nla actualizacion.",
        confirm_install = "Instalar",
        confirm_reinstall = "Reinstalar",
        cancel = "Cancelar",
        error = "Error",
        fetch_error = "Error al buscar versiones: %s",
        check_self_update = "Verificar Actualizacion del Instalador",
        checking_self_update = "Verificando actualizacion del instalador...",
        self_update_available = "Nueva version del instalador disponible!\n\nVersion actual: v%s\nNueva version: v%s\n\nDesea actualizar el instalador?",
        self_update_success = "Instalador actualizado a v%s!",
        self_update_failed = "Error al actualizar el instalador.\n\n%s",
        self_update_current = "Su instalador ya esta en la version mas reciente (v%s).",
        self_update_downloading = "Descargando actualizacion del instalador...",
        no_changelog = "No hay changelog disponible para esta version.",
        changelog_title = "Changelog - v%s"
    }
}

function S(key)
    local lang = STRINGS[gCurrentLang] or STRINGS["pt_br"]
    return lang[key] or STRINGS["pt_br"][key] or key
end

function main()
    if Aurora.HasInternetConnection() ~= true then
        Script.ShowMessageBox(S("no_network"), S("no_network_msg"), "OK")
        return
    end

    print("-- " .. scriptTitle .. " Started...")
    init()
    if not gLanguageSaved then
        HandleLanguageSelect()
        gLanguageSaved = true
    end
    MakeMainMenu()
    DoMainLoop()
    cleanup()
    print("-- " .. scriptTitle .. " Ended...")
end

function init()
    gGodStixPath = computeGodStixPath()
    gAbsoluteDownloadsPath = Script.GetBasePath() .. gDownloadsPath

    pcall(FileSystem.DeleteDirectory, gAbsoluteDownloadsPath)

    local ok, ini = pcall(IniFile.LoadFile, "GodStixInstaller.ini")
    if ok and ini then
        local savedUrl = ini:ReadValue("Settings", "ServerUrl", "")
        if savedUrl ~= "" then
            SERVER_URL = savedUrl
            API_BASE = SERVER_URL .. "/api"
        end
        local savedLang = ini:ReadValue("Settings", "Language", "")
        if savedLang ~= "" then
            gCurrentLang = savedLang
            gLanguageSaved = true
        end
    end
end

function cleanup()
    FileSystem.DeleteDirectory(gAbsoluteDownloadsPath)
end

function computeGodStixPath()
    local basePath = Script.GetBasePath()
    local stripped = basePath:gsub("[/\\]$", "")
    local parent = stripped:match("^(.*)[/\\][^/\\]+$")
    if parent then
        return parent .. "\\"
    end
    return basePath
end

function saveSettings()
    pcall(function()
        local ini = IniFile.LoadFile("GodStixInstaller.ini")
        if ini then
            ini:WriteValue("Settings", "ServerUrl", SERVER_URL)
            ini:WriteValue("Settings", "Language", gCurrentLang)
            ini:SaveFile("GodStixInstaller.ini")
        end
    end)
end

function MakeMainMenu()
    Menu.ResetMenu()
    Menu.SetTitle(S("title"))
    Menu.SetGoBackText("")
    Menu.SetSortAlphaBetically(false)
    Menu.AddMainMenuItem(Menu.MakeMenuItem(S("install_update"), { action = "install" }))
    Menu.AddMainMenuItem(Menu.MakeMenuItem(S("changelog"), { action = "changelog" }))
    Menu.AddMainMenuItem(Menu.MakeMenuItem(S("settings"), { action = "settings" }))
    Menu.AddMainMenuItem(Menu.MakeMenuItem(S("about"), { action = "about" }))
end

function DoMainLoop()
    local running = true
    while running do
        if gShouldExit then
            running = false
            return
        end
        MakeMainMenu()
        local ret, menu, canceled = Menu.ShowMainMenu()
        if canceled then
            running = false
        elseif ret and ret.action then
            if ret.action == "install" then
                HandleInstallUpdate()
            elseif ret.action == "changelog" then
                HandleChangelog()
            elseif ret.action == "settings" then
                HandleSettings()
            elseif ret.action == "about" then
                HandleAbout()
            end
        else
            running = false
        end
    end
end

function fetchReleases()
    Script.SetStatus(S("fetching_releases"))
    Script.SetProgress(0)

    local url = API_BASE .. "/releases"
    local http = Http.Get(url)

    if not http.Success then
        Script.SetProgress(100)
        Script.ShowMessageBox(S("error"), S("download_failed"), "OK")
        return nil
    end

    Script.SetProgress(50)
    local data = json:decode(http.OutputData)

    if not data or not data.success or not data.releases or #data.releases == 0 then
        Script.SetProgress(100)
        Script.ShowMessageBox(S("title"), S("no_releases"), "OK")
        return nil
    end

    Script.SetProgress(100)
    return data.releases
end

function getInstalledGodStixVersion()
    local iniPath = gGodStixPath .. "config.ini"
    local ok, ini = pcall(IniFile.LoadFile, iniPath)
    if ok and ini then
        local ver = ini:ReadValue("Script", "Version", "")
        if ver ~= "" then return ver end
    end

    local mainLuaPath = gGodStixPath .. "GODSend\\main.lua"
    if not FileSystem.FileExists(mainLuaPath) then
        mainLuaPath = gGodStixPath .. "main.lua"
    end
    if FileSystem.FileExists(mainLuaPath) then
        local ok2, content = pcall(FileSystem.ReadFile, mainLuaPath)
        if ok2 and content then
            local ver = content:match('scriptVersion%s*=%s*"([^"]+)"')
            if ver then return ver end
        end
    end

    return nil
end

function buildVersionMenuItems(releases)
    local menuItems = {}
    menuItems[1] = ">> " .. S("version_list_header")
    for i, rel in ipairs(releases) do
        local label = "v" .. (rel.version or "?")
        if rel.release_date then
            label = label .. " (" .. rel.release_date .. ")"
        end
        menuItems[i + 1] = label
    end
    return menuItems
end

function buildChangelogText(release)
    if not release.changelog or type(release.changelog) ~= "table" or #release.changelog == 0 then
        return nil
    end
    local lines = ""
    for i, item in ipairs(release.changelog) do
        if item.title and item.title ~= "" then
            if lines ~= "" then lines = lines .. "\n" end
            lines = lines .. "- " .. item.title
            if item.description and item.description ~= "" then
                lines = lines .. ": " .. item.description
            end
        end
    end
    if lines == "" then return nil end
    return lines
end

function HandleChangelog()
    local releases = fetchReleases()
    if not releases then return end

    local menuItems = buildVersionMenuItems(releases)

    local ret = Script.ShowPopupList(S("changelog"), "", menuItems)
    if ret.Canceled then return end

    if ret.Selected.Key == 1 then return end

    local selectedRelease = releases[ret.Selected.Key - 1]
    if not selectedRelease then return end

    local changelogText = buildChangelogText(selectedRelease)
    if not changelogText then
        Script.ShowMessageBox(
            string.format(S("changelog_title"), selectedRelease.version or "?"),
            S("no_changelog"),
            "OK")
        return
    end

    Script.ShowMessageBox(
        string.format(S("changelog_title"), selectedRelease.version or "?"),
        changelogText,
        "OK")
end

function HandleInstallUpdate()
    local releases = fetchReleases()
    if not releases then return end

    local menuItems = buildVersionMenuItems(releases)

    local ret = Script.ShowPopupList(S("select_version"), "", menuItems)
    if ret.Canceled then return end

    if ret.Selected.Key == 1 then return end

    local selectedRelease = releases[ret.Selected.Key - 1]
    if not selectedRelease then return end

    local installedVersion = getInstalledGodStixVersion()
    local isInstalled = installedVersion and installedVersion == selectedRelease.version

    local desc = selectedRelease.description or ""
    local dateStr = selectedRelease.release_date or "-"
    local dlCount = tostring(selectedRelease.download_count or 0)
    local infoMsg
    local confirmBtn

    if isInstalled then
        if desc ~= "" then
            infoMsg = string.format(S("version_info_reinstall"), selectedRelease.version, dateStr, dlCount, desc)
        else
            infoMsg = string.format(S("version_info_reinstall_no_desc"), selectedRelease.version, dateStr, dlCount)
        end
        confirmBtn = S("confirm_reinstall")
    else
        if desc ~= "" then
            infoMsg = string.format(S("version_info"), selectedRelease.version, dateStr, dlCount, desc)
        else
            infoMsg = string.format(S("version_info_no_desc"), selectedRelease.version, dateStr, dlCount)
        end
        confirmBtn = S("confirm_install")
    end

    local confirm = Script.ShowMessageBox(S("title"), infoMsg, confirmBtn, S("cancel"))
    if confirm.Canceled or confirm.Button ~= 1 then return end

    DoInstallRelease(selectedRelease)
end

function DoInstallRelease(release)
    local version = release.version or "unknown"
    local downloadUrl = release.download_url
    if not downloadUrl or downloadUrl == "" then
        Script.ShowMessageBox(S("error"), string.format(S("install_failed"), "No download URL"), "OK")
        return
    end

    local installPath = gGodStixPath
    local selection = { zipurl = downloadUrl }
    HandleZipInstall(selection, installPath, version)
end

function HandleZipInstall(selection, installPath, version)
    Script.SetStatus("Downloading Script...");
    Script.SetProgress(0);
    local dlpath = gDownloadsPath.."tmp.7z";
    local http = Http.Get(selection.zipurl, dlpath);
    if http.Success then
        Script.SetStatus("Extracting Script...");
        Script.SetProgress(25);
        local zip = ZipFile.OpenFile(dlpath);
        if zip == nil then
            Script.ShowMessageBox("ERROR", "Extraction failed! [OpenFile nil]\n\nPath: " .. tostring(dlpath), "OK");
            return false;
        end
        local result = zip.Extract(zip, gDownloadsPath.."tmp\\");
        FileSystem.DeleteFile(http.OutputPath);
        if result == false then
            Script.ShowMessageBox("ERROR", "Extraction failed! [Extract false]\n\nPath: " .. tostring(dlpath), "OK");
        else
            Script.SetStatus("Installing Script...");
            Script.SetProgress(75);
            result = FileSystem.MoveDirectory(gAbsoluteDownloadsPath.."tmp\\", installPath, true);
            Script.SetStatus("Done!");
            Script.SetProgress(100);
            if result == true then
                FileSystem.DeleteDirectory(gAbsoluteDownloadsPath);
                Script.ShowMessageBox(S("title"),
                    string.format(S("install_success"), version), "OK")
                gShouldExit = true
                return true;
            else
                Script.ShowMessageBox("ERROR", "Installation failed!", "OK");
            end
        end
    else
        Script.ShowMessageBox("ERROR", "Download failed\n\nPlease try again later...", "OK");
    end
    return false;
end

function findWebuiFolders(godstixDir)
    local result = {}
    local ok, items = pcall(FileSystem.GetFilesAndDirectories, godstixDir)
    if ok and items then
        for _, item in ipairs(items) do
            local dirName = item:match("([^/\\]+)[/\\]?$")
            if dirName then
                local lower = dirName:lower()
                local isDir = FileSystem.FileExists(godstixDir .. dirName .. "\\")
                if isDir and (lower == "webuis" or lower:find("^webuis_backup") or lower:find("^webui_backup") or lower:find("backup")) then
                    result[#result + 1] = dirName
                end
            end
        end
    end
    return result
end

function HandleSelfUpdate()
    Script.SetStatus(S("checking_self_update"))
    Script.SetProgress(0)

    local checkUrl = SERVER_URL .. "/api/installer-version"
    local httpCheck = Http.Get(checkUrl)

    if not httpCheck.Success then
        Script.SetProgress(100)
        Script.ShowMessageBox(S("error"), S("connection_failed"), "OK")
        return
    end

    Script.SetProgress(50)

    local installerUrl = SERVER_URL .. "/plugin/download-installer"
    local data = json:decode(httpCheck.OutputData)

    if not data or not data.version then
        Script.SetProgress(100)
        Script.ShowMessageBox(S("title"), string.format(S("self_update_current"), scriptVersion), "OK")
        return
    end

    local remoteVer = data.version
    if remoteVer == scriptVersion then
        Script.SetProgress(100)
        Script.ShowMessageBox(S("title"), string.format(S("self_update_current"), scriptVersion), "OK")
        return
    end

    local confirm = Script.ShowMessageBox(S("title"),
        string.format(S("self_update_available"), scriptVersion, remoteVer),
        S("confirm_install"), S("cancel"))

    if confirm.Canceled or confirm.Button ~= 1 then
        Script.SetProgress(100)
        return
    end

    Script.SetStatus(S("self_update_downloading"))
    Script.SetProgress(60)

    FileSystem.DeleteDirectory(gAbsoluteDownloadsPath)

    local dlPath = gDownloadsPath .. "installer_update.zip"
    local dlHttp = Http.Get(installerUrl, dlPath)

    if not dlHttp.Success then
        Script.SetProgress(100)
        Script.ShowMessageBox(S("error"), string.format(S("self_update_failed"), "Download failed"), "OK")
        return
    end

    Script.SetProgress(80)

    local zipPath = dlHttp.OutputPath or dlPath
    local zip = ZipFile.OpenFile(zipPath)
    if zip == nil then
        zip = ZipFile.OpenFile(dlPath)
    end
    if zip == nil then
        Script.SetProgress(100)
        Script.ShowMessageBox(S("error"), string.format(S("self_update_failed"), "ZipFile.OpenFile: nil"), "OK")
        return
    end

    local extractDir = gAbsoluteDownloadsPath .. "installer_tmp\\"
    local extractOk = zip.Extract(zip, extractDir)
    FileSystem.DeleteFile(dlHttp.OutputPath)

    if not extractOk then
        Script.SetProgress(100)
        Script.ShowMessageBox(S("error"), string.format(S("self_update_failed"), "Extract failed"), "OK")
        return
    end

    local installerBasePath = Script.GetBasePath()
    local iniPath = installerBasePath .. "GodStixInstaller.ini"
    local iniBackupPath = gAbsoluteDownloadsPath .. "GodStixInstaller.ini.bak"

    if FileSystem.FileExists(iniPath) then
        pcall(FileSystem.CopyFile, iniPath, iniBackupPath, true)
    end

    local srcDir = extractDir .. "GodStix Installer\\"
    if FileSystem.FileExists(srcDir) then
        FileSystem.MoveDirectory(srcDir, installerBasePath, true)
    end

    if FileSystem.FileExists(iniBackupPath) then
        pcall(FileSystem.CopyFile, iniBackupPath, iniPath, true)
    end

    FileSystem.DeleteDirectory(gAbsoluteDownloadsPath)
    Script.SetProgress(100)

    Script.ShowMessageBox(S("title"),
        string.format(S("self_update_success"), remoteVer), "OK")
    gShouldExit = true
end

function HandleSettings()
    local running = true
    while running do
        local menuItems = {
            S("back"),
            S("language") .. ": " .. getLanguageName(gCurrentLang),
            S("test_connection"),
            S("check_self_update")
        }

        local ret = Script.ShowPopupList(S("settings"), "", menuItems)
        if ret.Canceled or ret.Selected.Key == 1 then
            running = false
        elseif ret.Selected.Key == 2 then
            HandleLanguageSelect()
        elseif ret.Selected.Key == 3 then
            TestConnection()
        elseif ret.Selected.Key == 4 then
            HandleSelfUpdate()
            if gShouldExit then
                running = false
            end
        end
    end
end

function HandleLanguageSelect()
    local langNames = {}
    for i, lang in ipairs(LANGUAGES) do
        local label = lang.name
        if lang.code == gCurrentLang then
            label = label .. " *"
        end
        langNames[i] = label
    end

    local ret = Script.ShowPopupList(S("select_language"), "", langNames)
    if not ret.Canceled then
        gCurrentLang = LANGUAGES[ret.Selected.Key].code
        saveSettings()
    end
end

function TestConnection()
    Script.SetStatus(S("test_connection") .. "...")
    Script.SetProgress(0)

    local http = Http.Get(API_BASE .. "/ping")
    Script.SetProgress(100)

    if http.Success then
        Script.ShowMessageBox(S("title"), S("connection_ok"), "OK")
    else
        Script.ShowMessageBox(S("error"), S("connection_failed"), "OK")
    end
end

function HandleAbout()
    local msg = string.format(S("about_text"), scriptVersion, scriptAuthor)
    Script.ShowMessageBox(S("title"), msg, "OK")
end

function getLanguageName(code)
    for _, lang in ipairs(LANGUAGES) do
        if lang.code == code then return lang.name end
    end
    return code
end
